from flask import Flask, jsonify, request
import db

app = Flask(__name__)


# SHOW ALL TASKS
@app.route('/api/tasks')
def get_tasks():
    tasks = db.query('SELECT * from tasks')
    print(tasks)
    return jsonify(tasks)


# SHOW TASK BY ID
@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    task = db.query('SELECT * FROM tasks WHERE id=?', (id,))
    if task:
        return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404


# CREATE TASK
@app.route('/api/tasks', methods=['POST'])
def create_task():
    new_task = request.json
    title = new_task.get('title')
    if title:
        db.query('''INSERT INTO tasks (title) VALUES (?)''', (title,))
        return jsonify({'title': title, 'message': 'Task added successfully'}), 201
    else:
        return jsonify({'error': 'Title is missing in the request data'}), 400


# UPDATE TASK
@app.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task_data = request.json
    new_title = task_data.get('title')
    if new_title:
        existing_task = db.query('SELECT * FROM tasks WHERE id=?', (id,))
        if existing_task:
            db.query('UPDATE tasks SET title=? WHERE id=?', (new_title, id))
            return jsonify({'message': 'Task updated successfully'})
        else:
            return jsonify({'message': 'Task not found'}), 404
    else:
        return jsonify({'error': 'Title is missing in the request data'}), 400


# DELETE TASK
@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = db.query('SELECT * FROM tasks WHERE id=?', (id,))
    if task:
        db.query('DELETE FROM tasks WHERE id=?', (id,))
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
