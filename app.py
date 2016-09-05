#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'first',
    },
    {
        'id': 2,
        'title': u'second',
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title']
    }
    tasks.append(task)
    return jsonify({'task': tasks}), 201

if __name__ == '__main__':
    app.run(debug=True)
