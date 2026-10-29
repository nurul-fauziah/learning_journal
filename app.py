from flask import Flask, render_template, request, redirect, url_for, jsonify, abort, session
from flask_wtf.csrf import CSRFProtect, CSRFError
from models import db, User, Category, Entry, Reflection
from datetime import datetime, date, timedelta
from collections import defaultdict
import secrets
import os
import time
import re

app = Flask(__name__)

# --- Security Configuration ---
# 1. Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning_journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 2. Maximum Payload Size Limit (8 MB)
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

# 3. Session Security
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# 4. Persistent Cryptographic Secret Key
os.makedirs(app.instance_path, exist_ok=True)
secret_key_file = os.path.join(app.instance_path, 'secret_key')
if os.path.exists(secret_key_file):
    try:
        with open(secret_key_file, 'r', encoding='utf-8') as f:
            app.config['SECRET_KEY'] = f.read().strip()
    except Exception:
        app.config['SECRET_KEY'] = secrets.token_hex(32)
else:
    new_secret = secrets.token_hex(32)
    with open(secret_key_file, 'w', encoding='utf-8') as f:
        f.write(new_secret)
    app.config['SECRET_KEY'] = new_secret

# 5. CSRF Protection
csrf = CSRFProtect(app)

# 6. Initialize Database
db.init_app(app)

# --- Rate Limiting (In-Memory IP Bucket) ---
request_history = defaultdict(list)

def is_rate_limited(ip, limit=80, window=60):
    """Allow up to `limit` actions per `window` seconds per IP."""
    now = time.time()
    request_history[ip] = [t for t in request_history[ip] if now - t < window]
    if len(request_history[ip]) >= limit:
        return True
    request_history[ip].append(now)
    return False

@app.before_request
def rate_limit_check():
    """Apply rate limiting to all state-changing (POST) and API requests."""
    if request.method == 'POST' or request.path.startswith('/api/'):
        client_ip = request.headers.get('X-Forwarded-For', request.remote_addr or '127.0.0.1').split(',')[0].strip()
        if is_rate_limited(client_ip, limit=80, window=60):
            if request.is_json or request.path.startswith('/api/'):
                return jsonify({'error': 'Rate limit exceeded. Please wait a moment.'}), 429
            abort(429, description="Too many requests. Please slow down.")

# --- Authentication Guard Middleware ---
@app.before_request
def enforce_authentication():
    """Ensure all core routes require an authenticated session."""
    public_endpoints = {'login', 'register', 'static'}
    if request.endpoint in public_endpoints:
        return

    # If no accounts exist yet in DB, direct to first-time setup
    if User.query.count() == 0:
        if request.endpoint != 'register':
            return redirect(url_for('register'))
        return

    # Check logged-in session
    if not session.get('user_id'):
        if request.is_json or request.path.startswith('/api/'):
            return jsonify({'error': 'Authentication required. Please sign in.'}), 401
        return redirect(url_for('login', next=request.path))

# --- Security Headers Middleware ---
@app.after_request
def set_security_headers(response):
    """Enforce defensive HTTP security headers against XSS, clickjacking, and MIME sniffing."""
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net; "
        "img-src 'self' data:; "
        "connect-src 'self';"
    )
    return response

# --- CSRF Error Handler ---
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    if request.is_json or request.path.startswith('/api/'):
        return jsonify({'error': 'CSRF verification failed or session expired. Please refresh the page.'}), 400
    return render_template('add_entry.html', categories=Category.query.all(), error="Session expired. Please refresh the page and try again."), 400

# --- Template Filters ---
@app.template_filter('due_status')
def filter_due_status(target_dt):
    """Format target datetime into a human-friendly due label."""
    if not target_dt:
        return "Not scheduled"
    
    today = date.today()
    target_date = target_dt.date() if isinstance(target_dt, datetime) else target_dt
    diff_days = (target_date - today).days
    
    if diff_days < 0:
        return f"Overdue ({abs(diff_days)}d)"
    elif diff_days == 0:
        return "Due today"
    elif diff_days == 1:
        return "Due tomorrow"
    else:
        return f"Due in {diff_days}d"

# --- Helper Functions ---
def get_current_user_id():
    return session.get('user_id')

def calculate_streak(user_id):
    """Calculate consecutive days of learning activity for current user."""
    entry_dates = {e[0].date() for e in db.session.query(Entry.created_at).filter(Entry.user_id == user_id).all() if e[0]}
    reflection_dates = {r[0] for r in db.session.query(Reflection.date).filter(Reflection.user_id == user_id).all() if r[0]}
    activity_dates = entry_dates.union(reflection_dates)
    
    if not activity_dates:
        return 0
        
    today = date.today()
    yesterday = today - timedelta(days=1)
    
    if today not in activity_dates and yesterday not in activity_dates:
        return 0
        
    current_check = today if today in activity_dates else yesterday
    streak = 0
    while current_check in activity_dates:
        streak += 1
        current_check -= timedelta(days=1)
        
    return streak

def get_heatmap_data(user_id):
    """Generate activity counts for the last 30 days for current user."""
    heatmap_data = {}
    today = date.today()
    
    for i in range(29, -1, -1):
        d = today - timedelta(days=i)
        heatmap_data[d.strftime('%Y-%m-%d')] = 0
    
    start_date = today - timedelta(days=29)
    start_dt = datetime.combine(start_date, datetime.min.time())
    
    recent_entries = Entry.query.filter(Entry.user_id == user_id, Entry.created_at >= start_dt).all()
    for entry in recent_entries:
        if entry.created_at:
            k = entry.created_at.date().strftime('%Y-%m-%d')
            if k in heatmap_data:
                heatmap_data[k] += 1
                
    recent_reflections = Reflection.query.filter(Reflection.user_id == user_id, Reflection.date >= start_date).all()
    for ref in recent_reflections:
        if ref.date and ref.learned_today and ref.learned_today.strip():
            k = ref.date.strftime('%Y-%m-%d')
            if k in heatmap_data:
                heatmap_data[k] += 1
                
    return heatmap_data

# --- Authentication Routes ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('dashboard'))

    next_url = request.args.get('next') or request.form.get('next') or url_for('dashboard')
    error = None

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        remember = bool(request.form.get('remember'))

        user = User.query.filter(db.func.lower(User.username) == username.lower()).first()
        if user and user.check_password(password):
            session.clear()
            session['user_id'] = user.id
            session['username'] = user.username
            if remember:
                session.permanent = True
            return redirect(next_url)
        else:
            error = "Invalid username or password. Please verify and try again."

    return render_template('login.html', error=error, next_url=next_url)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        return redirect(url_for('dashboard'))

    error = None
    is_first_user = User.query.count() == 0

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not username or len(username) < 3:
            error = "Username must be at least 3 characters long."
        elif len(username) > 30:
            error = "Username cannot exceed 30 characters."
        elif not re.match(r'^[a-zA-Z0-9_]+$', username):
            error = "Username may only contain letters, numbers, and underscores."
        elif len(password) < 6:
            error = "Password must be at least 6 characters long."
        elif password != confirm_password:
            error = "Passwords do not match."
        elif User.query.filter(db.func.lower(User.username) == username.lower()).first():
            error = "This username is already taken. Please choose another."
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            # Associate any existing unassigned notes to this first user
            Entry.query.filter(Entry.user_id.is_(None)).update({Entry.user_id: new_user.id}, synchronize_session=False)
            Reflection.query.filter(Reflection.user_id.is_(None)).update({Reflection.user_id: new_user.id}, synchronize_session=False)
            db.session.commit()

            session.clear()
            session['user_id'] = new_user.id
            session['username'] = new_user.username
            session.permanent = True
            return redirect(url_for('dashboard'))

    return render_template('register.html', error=error, is_first_user=is_first_user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# --- Core Application Routes ---

@app.route('/')
def dashboard():
    user_id = get_current_user_id()
    total_entries = Entry.query.filter_by(user_id=user_id).count()
    now = datetime.now()
    due_reviews = Entry.query.filter(Entry.user_id == user_id, Entry.next_review <= now).count()
    streak_count = calculate_streak(user_id)
    heatmap_data = get_heatmap_data(user_id)
    
    return render_template(
        'dashboard.html', 
        total=total_entries, 
        due=due_reviews, 
        streak=streak_count,
        heatmap=heatmap_data
    )

@app.route('/vault')
def vault():
    user_id = get_current_user_id()
    entries = Entry.query.filter_by(user_id=user_id).order_by(Entry.created_at.desc()).all()
    categories = Category.query.all()
    return render_template('vault.html', entries=entries, categories=categories, now=datetime.now())

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    user_id = get_current_user_id()
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        category_name = request.form.get('category', '').strip()
        summary = request.form.get('summary', '').strip()
        content = request.form.get('content', '').strip()
        difficulty = request.form.get('difficulty', 'medium').strip().lower()

        categories = Category.query.all()
        if not title or not category_name or not summary:
            return render_template('add_entry.html', categories=categories, error="Please complete all required fields."), 400

        if len(title) > 150:
            return render_template('add_entry.html', categories=categories, error="Title cannot exceed 150 characters."), 400

        if len(category_name) > 50:
            return render_template('add_entry.html', categories=categories, error="Category name cannot exceed 50 characters."), 400

        if len(summary) > 250:
            return render_template('add_entry.html', categories=categories, error="Summary cannot exceed 250 characters."), 400

        if len(content) > 15000:
            return render_template('add_entry.html', categories=categories, error="Content length cannot exceed 15,000 characters."), 400

        if difficulty not in ['easy', 'medium', 'hard']:
            difficulty = 'medium'

        cat = Category.query.filter(db.func.lower(Category.name) == category_name.lower()).first()
        if not cat:
            cat = Category(name=category_name)
            db.session.add(cat)
            db.session.commit()

        initial_days = 1 if difficulty == 'hard' else 2 if difficulty == 'medium' else 4
        next_review_time = datetime.now() + timedelta(days=initial_days)

        new_entry = Entry(
            title=title, 
            category=cat, 
            summary=summary,
            content=content, 
            difficulty=difficulty,
            user_id=user_id,
            review_count=0,
            next_review=next_review_time,
            created_at=datetime.now()
        )
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('vault'))
    
    categories = Category.query.all()
    return render_template('add_entry.html', categories=categories)

@app.route('/review_session')
def review_session():
    user_id = get_current_user_id()
    now = datetime.now()
    due_entries = Entry.query.filter(Entry.user_id == user_id, Entry.next_review <= now).all()
    is_practice = False
    
    if not due_entries:
        due_entries = Entry.query.filter_by(user_id=user_id).order_by(db.func.random()).limit(5).all()
        is_practice = bool(due_entries)
    
    return render_template('review.html', entries=due_entries, is_practice=is_practice)

@app.route('/api/mark_reviewed/<int:id>', methods=['POST'])
def mark_reviewed(id):
    user_id = get_current_user_id()
    entry = Entry.query.filter_by(id=id, user_id=user_id).first_or_404()
    data = request.get_json(silent=True) or {}
    quality = str(data.get('quality', 'medium')).lower()

    if quality not in ['easy', 'medium', 'hard']:
        quality = 'medium'

    now = datetime.now()
    if quality == 'easy':
        days = 3 + (entry.review_count * 2)
        entry.review_count += 1
    elif quality == 'medium':
        days = 1 + entry.review_count
        entry.review_count += 1
    else:  # 'hard'
        days = 1
        entry.review_count = max(0, entry.review_count - 1)
    
    entry.next_review = now + timedelta(days=days)
    db.session.commit()
    
    return jsonify({
        'status': 'success', 
        'next_date': entry.next_review.strftime('%Y-%m-%d %H:%M'),
        'review_count': entry.review_count
    })

# --- API for Reflection ---
@app.route('/api/reflection', methods=['GET', 'POST'])
def api_reflection():
    user_id = get_current_user_id()
    today = date.today()
    reflection = Reflection.query.filter_by(date=today, user_id=user_id).first()
    
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        text = str(data.get('text', '')).strip()

        if len(text) > 5000:
            return jsonify({'error': 'Reflection text exceeds 5,000 characters maximum limit.'}), 400
        
        if not reflection:
            reflection = Reflection(date=today, learned_today=text, user_id=user_id)
            db.session.add(reflection)
        else:
            reflection.learned_today = text
            
        db.session.commit()
        return jsonify({
            'status': 'success', 
            'saved_at': datetime.now().strftime('%H:%M')
        })
        
    return jsonify({
        'date': today.strftime('%Y-%m-%d'),
        'learned_today': reflection.learned_today if reflection else ''
    })

# --- API for Alarm Trigger ---
@app.route('/api/random_question')
def get_random_question():
    user_id = get_current_user_id()
    entry = Entry.query.filter_by(user_id=user_id).order_by(db.func.random()).first()
    if entry:
        return jsonify({
            'id': entry.id,
            'question': entry.title,
            'answer': entry.summary
        })
    return jsonify(None)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    debug_mode = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='127.0.0.1', port=5000, debug=debug_mode)
