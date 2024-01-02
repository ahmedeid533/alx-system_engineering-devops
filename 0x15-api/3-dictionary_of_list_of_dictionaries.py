#!/usr/bin/python3
"""Export data in the JSON format."""


if __name__ == "__main__":
    """Export data in the JSON format."""
    import requests
    import json

    AllempTasks = {}
    url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(url).json()

    for user in users:
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user['id'])
        tasks = requests.get(url).json()
        tasks_list = []
        for task in tasks:
            tasks_list.append({"username": user['username'],
                               "task": task['title'],
                               "completed": task['completed']})
        AllempTasks[user['id']] = tasks_list
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(AllempTasks, jsonfile)
