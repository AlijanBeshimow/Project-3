from flask import Flask, jsonify, request, send_file
import db

app = Flask(__name__)


# BASE
@app.route('/')
def base():
    return send_file("static/index.html")


# SHOW ALL TASKS
@app.route('/api/tasks')
def get_tasks():
    tasks = db.query('SELECT id, title, description, category FROM tasks')
    tasks_list = [{'id': task[0], 'title': task[1],
                   'description': task[2], 'category': task[3]} for task in tasks]
    return jsonify({'tasks': tasks_list})


# SHOW TASK BY ID
@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    task = db.query('SELECT * FROM tasks WHERE id=?', (id,))
    if task:
        task_dict = {'id': task[0][0], 'title': task[0][1],
                     'description': task[0][2], 'category': task[0][3]}
        return jsonify(task_dict)
    return jsonify({'message': 'Task not found'}), 404


# CREATE TASK
@app.route('/api/tasks', methods=['POST'])
def create_task():
    new_task = request.json
    title = new_task.get('title')
    description = new_task.get('description')
    category = new_task.get('category')
    if title is not None and description is not None and category is not None:
        db.query('''INSERT INTO tasks (title, description, category) VALUES (?,?,?)''',
                 (title, description, category,))
        return jsonify({'message': 'Task added successfully'}), 201
    else:
        return jsonify({'error': 'Title, description, or category is missing in the request data'}), 400


# UPDATE TASK
@app.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task_data = request.json
    new_title = task_data.get('title')
    new_description = task_data.get('description')
    new_category = task_data.get('category')

    if new_title is None:
        return jsonify({'error': 'Title is missing in the request data'}), 400

    existing_task = db.query('SELECT * FROM tasks WHERE id=?', (id,))

    if not existing_task:
        return jsonify({'message': 'Task not found'}), 404

    update_values = []
    if new_title:
        update_values.append(new_title)
    else:
        update_values.append(existing_task['title'])
    if new_description:
        update_values.append(new_description)
    else:
        update_values.append(existing_task['description'])
    if new_category:
        update_values.append(new_category)
    else:
        update_values.append(existing_task['category'])

    db.query('UPDATE tasks SET title=?, description=?, category=? WHERE id=?',
             (update_values[0], update_values[1], update_values[2], id))

    return jsonify({'message': 'Task updated successfully'})


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
