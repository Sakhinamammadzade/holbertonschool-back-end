#!/usr/bin/python3
"""Exporting data in json format"""

import json
import requests
from sys import argv


def export_data():
    """exporting data in the JSON"""
    users_route = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_route = 'https://jsonplaceholder.typicode.com/todos/?userID={}'
    users_url = users_route.format(argv[1])
    todos_url = todos_route.format(argv[1])
    user_data = requests.get(users_url).json()
    task_data = requests.get(todos_url).json()
    username = user_data.get('username')
    tasks = []

    for todo in task_data:
        task = {'task': todo.get('title'),
                'completed': todo.get('completed'),
                'username': username}
        tasks.append(task)

    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump({argv[1]: tasks}, file)


if __name__ == "__main__":
    export_data()
