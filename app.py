from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import db, Category, Entry, Reflection
from datetime import datetime, timedelta
import random

app = Flask(__name__)
# Pastikan path database benar
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning_journal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# --- Helper Functions ---
def get_heatmap_data():
    """Mengenerate data dummy/real untuk heatmap 30 hari terakhir"""
    heatmap_data = {}
    today = datetime.utcnow().date()
    
    # Inisialisasi 30 hari terakhir dengan nilai 0
    for i in range(29, -1, -1):
        date = today - timedelta(days=i)
        heatmap_data[date.strftime('%Y-%m-%d')] = 0
    
    # Ambil data entry yang dibuat 30 hari terakhir
    recent_entries = Entry.query.filter(Entry.created_at >= (datetime.utcnow() - timedelta(days=30))).all()
    
    for entry in recent_entries:
        date_key = entry.created_at.strftime('%Y-%m-%d')
        if date_key in heatmap_data:
            heatmap_data[date_key] += 1
            
    return heatmap_data

# --- Routes ---

@app.route('/')
def dashboard():
    # Hitung streak & stats sederhana
    total_entries = Entry.query.count()
    due_reviews = Entry.query.filter(Entry.next_review <= datetime.utcnow()).count()
    
    # Ambil data heatmap
    heatmap_data = get_heatmap_data()
    
    return render_template('dashboard.html', 
                           total=total_entries, 
                           due=due_reviews, 
                           heatmap=heatmap_data)

@app.route('/vault')
def vault():
    # Mengirim 'now' agar template bisa menghitung sisa hari
    entries = Entry.query.order_by(Entry.created_at.desc()).all()
    categories = Category.query.all()
    return render_template('vault.html', entries=entries, categories=categories, now=datetime.utcnow())

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        title = request.form['title']
        category_name = request.form['category']
        summary = request.form['summary']
        content = request.form['content']
        difficulty = request.form['difficulty']

        # Handle Category (Create if new/unik)
        cat = Category.query.filter_by(name=category_name).first()
        if not cat:
            cat = Category(name=category_name)
            db.session.add(cat)
            db.session.commit()

        new_entry = Entry(
            title=title, category=cat, summary=summary,
            content=content, difficulty=difficulty
        )
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('vault'))
    
    categories = Category.query.all()
    return render_template('add_entry.html', categories=categories)

@app.route('/review_session')
def review_session():
    # Ambil materi yang sudah waktunya di-review
    due_entries = Entry.query.filter(Entry.next_review <= datetime.utcnow()).all()
    
    # Jika tidak ada yang due, ambil 5 soal random untuk latihan
    if not due_entries:
        due_entries = Entry.query.order_by(db.func.random()).limit(5).all()
    
    return render_template('review.html', entries=due_entries)

@app.route('/api/mark_reviewed/<int:id>', methods=['POST'])
def mark_reviewed(id):
    entry = Entry.query.get_or_404(id)
    data = request.json
    quality = data.get('quality') # 'easy', 'medium', 'hard'

    # Logic Spaced Repetition Sederhana
    if quality == 'easy':
        days = 3 + (entry.review_count * 2)
    elif quality == 'medium':
        days = 1 + entry.review_count
    else: # hard / fail
        days = 0 # Review again immediately/tomorrow
    
    entry.next_review = datetime.utcnow() + timedelta(days=days)
    entry.review_count += 1
    db.session.commit()
    
    return jsonify({'status': 'success', 'next_date': entry.next_review})

# --- API untuk Alarm Trigger ---
@app.route('/api/random_question')
def get_random_question():
    entry = Entry.query.order_by(db.func.random()).first()
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
    app.run(debug=True)
