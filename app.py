from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import spacy
from models import db, Task  # Import db and Task model

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db with app
db.init_app(app)

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Ensure database is created inside an app context
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # Generate AI Summary (first sentence only)
        doc = nlp(description)
        summary = " ".join([sent.text for sent in doc.sents][:1])  # First sentence

        # Save to DB
        new_task = Task(title=title, description=description, summary=summary)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add_task.html')

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/view_task/<int:task_id>')
def view_task(task_id):
    task = Task.query.get_or_404(task_id)  # Fetch task or return 404
    return render_template('view_task.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)
