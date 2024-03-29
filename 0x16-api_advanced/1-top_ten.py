#!/usr/bin/python3
"""Get top ten hot posts"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code >= 300:
        print('None')
    else:
        for post in r.json().get('data').get('children'):
            print(post.get('data').get('title'))
