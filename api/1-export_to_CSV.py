#!/usr/bin/python3
"""Exports data in CSV  format"""


import csv
import requests
import sys


def export_data():
    """method to export related data"""
    user_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user).json().get('username')
    todo_requests = requests.get(todos).json()

    with open('{}.csv'.format(user_id), 'w') as file:
        for todo in todo_requests:
            info = '"{}","{}","{}","{}"\n'.format(
                user_id, name, todo.get('completed'), todo.get('title'))
            file.write(info)


if __name__ == "__main__":
    export_data()
