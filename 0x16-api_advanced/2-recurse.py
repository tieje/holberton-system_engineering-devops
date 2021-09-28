#!/usr/bin/python3
"""returns all hot posts of a subreddit recursively"""
import requests


def recurse(subreddit, hot_list=[], after="NULL"):
    """returns all hot posts of a subreddit recursively"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Python:sub.counter:v1 (by /u/stoleitfirst)'}
    param = {'after': after}
    res = requests.get(url, headers=header, params=param,
                       allow_redirects=False).json()
    try:
        for post in res['data']['children']:
            hot_list.append(post['data']['title'])
    except:
        return None
    after = res['data']['after']
    if after not in [None, 'None', 'NULL']:
        return recurse(subreddit, hot_list, after)
    return hot_list
