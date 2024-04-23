#!/usr/bin/python3
"""exporting data in json format"""


import json
import requests


def export_data():
    """Saving all the data to JSON file"""
    users_route = 'https://jsonplaceholder.typicode.com/users'
    todos_route = 'https://jsonplaceholder.typicode.com/todos/?userID={}'
    users = requests.get(users_route).json()
    data = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todos = todos_route.format(user_id)
        todo_request = requests.get(todos).json()
        tasks = []
        for todo in todo_request:
            task = {"username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')}
            tasks.append(task)
        data[user_id] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    export_data()
