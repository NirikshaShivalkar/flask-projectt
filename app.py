from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store tasks in memory
tasks = []

# Home Route - Display tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Add Task
@app.route('/add', methods=['POST'])
def add_task():
    content = request.form['content']
    if content:
        tasks.append({'content': content, 'completed': False})
    return redirect(url_for('index'))

# Delete Task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

# Mark Task as Completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = not tasks[task_id]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
