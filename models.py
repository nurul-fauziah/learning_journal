from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

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
    difficulty = db.Column(db.String(20), default='medium') # easy, medium, hard
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    # Spaced Repetition Fields
    review_count = db.Column(db.Integer, default=0)
    next_review = db.Column(db.DateTime, default=datetime.now)
    
class Reflection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today, unique=True)
    learned_today = db.Column(db.Text)
    confused_about = db.Column(db.Text)
