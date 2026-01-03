from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    entries = db.relationship('Entry', backref='category', lazy=True)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False) # Detail materi
    summary = db.Column(db.String(200)) # Ringkasan/Jawaban singkat
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    difficulty = db.Column(db.String(20)) # Easy, Medium, Hard
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Spaced Repetition Fields
    review_count = db.Column(db.Integer, default=0)
    next_review = db.Column(db.DateTime, default=datetime.utcnow)
    
class Reflection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow().date, unique=True)
    learned_today = db.Column(db.Text)
    confused_about = db.Column(db.Text)
