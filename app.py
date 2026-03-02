from flask import Flask, render_template, request, redirect, url_for
from models.todo import TodoItem, TodoManager

app = Flask(__name__)
todo_manager = TodoManager()  # Global manager

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('description')
        due = request.form.get('due_date')
        item = TodoItem(title, desc, due)
        todo_manager.add(item)
    todos = todo_manager.get_all()
    return render_template('index.html', todos=todos)

@app.route('/complete/<int:index>')
def complete(index):
    todo = todo_manager.get_all()[index]
    todo.mark_as_completed()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
