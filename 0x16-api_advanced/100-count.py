#!/usr/bin/python3
"""Count words"""


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Count words"""
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102\
               Safari/537.36'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    for post in r.json().get('data').get('children'):
        hot_list.append(post.get('data').get('title'))
    after = r.json().get('data').get('after')
    if after is None:
        return hot_list
    return count_words(subreddit, word_list, hot_list, after)
