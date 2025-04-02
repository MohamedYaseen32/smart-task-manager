from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Don't pass the app here

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text)  # AI-generated summary
