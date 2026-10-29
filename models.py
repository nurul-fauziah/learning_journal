from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    entries = db.relationship('Entry', backref='author', lazy=True)
    reflections = db.relationship('Reflection', backref='author', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    entries = db.relationship('Entry', backref='category', lazy=True)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False) # Detail materi
    summary = db.Column(db.String(250), nullable=False) # Ringkasan / Kunci jawaban
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    difficulty = db.Column(db.String(20), default='medium') # easy, medium, hard
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    # Spaced Repetition Fields
    review_count = db.Column(db.Integer, default=0)
    next_review = db.Column(db.DateTime, default=datetime.now)
    
class Reflection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    date = db.Column(db.Date, default=date.today)
    learned_today = db.Column(db.Text)
    confused_about = db.Column(db.Text)
