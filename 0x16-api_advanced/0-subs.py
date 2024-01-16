#!/usr/bin/python3
"""Get number of subscribers"""


def number_of_subscribers(subreddit):
    """Get number of subscribers"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0\
               (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
               (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36\
               Edge/12.246'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code >= 300:
        return 0

    return r.json().get('data').get('subscribers')
