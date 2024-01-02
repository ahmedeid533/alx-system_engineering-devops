#!/usr/bin/python3
"""Gather data from an API."""


if __name__ == "__main__":
    """Gather data from an API."""
    import requests
    import sys

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user = requests.get(url).json()
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)
    tasks = requests.get(url).json()
    completed_tasks = [task for task in tasks if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(
        user.get('name'), len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
