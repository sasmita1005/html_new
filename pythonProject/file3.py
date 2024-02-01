from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (in-memory database)
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'This is task 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'This is task 2',
        'done': False
    }
]

# Endpoint for getting all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Endpoint for creating a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'id': len(tasks) + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(new_task)
    return jsonify({'task': new_task}), 201

# Endpoint for updating a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404

    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])

    return jsonify({'task': task})

# Endpoint for deleting a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
