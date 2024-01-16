#!/usr/bin/python3
"""Get top ten hot posts"""


def top_ten(subreddit):
    """Get top ten hot posts"""
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K)\
               AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/114.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code >= 200:
        print("None")
        return
    for post in r.json().get('data').get('children'):
        print(post.get('data').get('title'))
