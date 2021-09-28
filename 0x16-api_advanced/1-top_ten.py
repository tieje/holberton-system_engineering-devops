#!/usr/bin/python3
"""return top 10 posts"""
import requests


def top_ten(subreddit):
    """returns top 10 posts of a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Python:sub.counter:v1 (by /u/stoleitfirst)'}
    param = {'limit': 10}
    try:
        sub_top = requests.get(url, headers=header, params=param,
                                allow_redirects=False).json()
        for post in sub_top['data']['children']:
            print(post['data']['title'])
    except:
        print(None)
