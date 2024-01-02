#!/usr/bin/python3
"""Export data in the JSON format."""


if __name__ == "__main__":
	"""Export data in the JSON format."""
	import requests
	import json
	
	AllempTasks = []
	for user_id in range(1, 11):
		#Get the user name
		url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
		user = requests.get(url).json()
		#Get the tasks
		url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
			user_id)
		tasks = requests.get(url).json()
		#Get the completed tasks
		completed_tasks = [task for task in tasks if task.get('completed') is True]
		#Print the information
		print('Employee {} is done with tasks({}/{}):'.format(
			user.get('name'), len(completed_tasks), len(tasks)))
		#Print the tasks
		for task in completed_tasks:
			print('\t {}'.format(task.get('title')))
		#Export the information to json
		AllempTasks.append({user_id: [{
			'username': user.get('username'),
			'task': task.get('title'),
			'completed': task.get('completed')} for task in tasks]})
	with open('todo_all_employees.json', 'w') as jsonfile:
			json.dump(AllempTasks, jsonfile)	
		