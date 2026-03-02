from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from datetime import date 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.Date)
    completed = db.Column(db.Boolean, default=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_str = request.form['due_date']  # String van form
        due_date = date.fromisoformat(due_str) if due_str else None  # → date object!
        
        new_todo = TodoItem(title=title, description=description, due_date=due_date)
        db.session.add(new_todo)
        db.session.commit()
    
    todos = TodoItem.query.all()
    return render_template('index.html', todos=todos)


@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = TodoItem.query.get(todo_id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Maak DB/tabel
    app.run(debug=True)

