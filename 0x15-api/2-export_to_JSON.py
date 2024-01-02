#!/usr/bin/python3
"""Export data in the JSON format."""


if __name__ == "__main__":
	"""Export data in the JSON format."""
	import requests
	import sys
	import json

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

	with open('{}.json'.format(user_id), 'w') as jsonfile:
		json.dump({user_id: [{
			'task': task.get('title'),
			'completed': task.get('completed'),
			'username': user.get('username')} for task in tasks]}, jsonfile)