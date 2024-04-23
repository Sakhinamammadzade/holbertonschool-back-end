#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


def fetch_data():
    """fetch data """
    user_id = sys.argv[1]
    users_route = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_route = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
    user = users_route.format(user_id)
    todos = todos_route.format(user_id)
    name = requests.get(user).json().get('name')
    todos_request = requests.get(todos).json()
    tasks = [task.get('title') for task in todos_request
             if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(name,
          len(tasks), len(todos_request)))
    print('\n'.join('\t {}'.format(task) for task in tasks))


if __name__ == "__main__":
    fetch_data()
