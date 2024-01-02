#!/usr/bin/python3
"""Export data in the JSON format."""


if __name__ == "__main__":
    """Export data in the JSON format."""
    import requests
    import json

    AllempTasks = []
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()

    for user in users:
        url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            user['id'])
        tasks = requests.get(url).json()

        completed_tasks = [task for task in tasks if task.get('completed')
                           is True]

        print('Employee {} is done with tasks({}/{}):'.format(
            user.get('name'), len(completed_tasks), len(tasks)))

        for task in completed_tasks:
            print('\t {}'.format(task.get('title')))

        AllempTasks.append({user['id']: [{
            'username': user.get('username'),
            'task': task.get('title'),
            'completed': task.get('completed')} for task in tasks]})
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(AllempTasks, jsonfile)
