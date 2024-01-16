#!/usr/bin/python3
"""Get number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My-User-Agent'}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code >= 300:
        return 0
    return r.json().get('data').get('subscribers')
