#!/usr/bin/python3
"""Export data in the CSV format."""


if __name__ == "__main__":
    """Export data in the CSV format."""
    import requests
    import sys
    import csv

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

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, user.get('username'),
                            task.get('completed'), task.get('title')])
