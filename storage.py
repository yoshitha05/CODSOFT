import json
from tasks import Task

FILENAME = 'tasks.json'

def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump([task.to_dict() for task in tasks], f)

def load_tasks():
    try:
        with open(FILENAME, 'r') as f:
            return [Task.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        return []
