#!/usr/bin/python3
"""
Saving to CSV
"""

if __name__ == '__main__':
    import requests
    import json

    user_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={:d}"

    ids_resp = requests.get(user_url).json()
    ids = [
            {
                "id": int(resp.get("id")), "username": resp.get("username")
                } for resp in ids_resp
            ]

    final_dict = dict()

    for obj in ids:
        todos = requests.get(todos_url.format(obj["id"])).json()
        tasks = [{
            "username": obj["username"],
            "task": todo.get("title"),
            "completed": todo.get("completed")
            } for todo in todos]
        final_dict |= {str(obj["id"]): tasks}

    with open("todo_all_employees.json", "w") as fp:
        fp.write(json.dumps(final_dict))
