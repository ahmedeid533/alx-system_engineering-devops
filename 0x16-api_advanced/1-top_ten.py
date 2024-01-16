#!/usr/bin/python3
"""Get top ten hot posts"""


def top_ten(subreddit):
    """Get top ten hot posts"""
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102\
               Safari/537.36'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    for post in r.json().get('data').get('children'):
        print(post.get('data').get('title'))
