#import requests
import requests
import sys

if __name__ == "__main__":
	# Get the user id
	user_id = sys.argv[1]
	# Get the user name
	url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
	user = requests.get(url).json()
	# Get the tasks
	url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
		user_id)
	tasks = requests.get(url).json()
	# Get the completed tasks
	completed_tasks = [task for task in tasks if task.get('completed') is True]
	# Print the information
	print('Employee {} is done with tasks({}/{}):'.format(
		user.get('name'), len(completed_tasks), len(tasks)))
	# Print the tasks
	for task in completed_tasks:
		print('\t {}'.format(task.get('title')))
