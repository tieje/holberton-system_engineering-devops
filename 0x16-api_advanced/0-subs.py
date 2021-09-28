#!/usr/bin/python3
'''gets number of subscribers for a given sub-reddit API'''
import requests


def number_of_subscribers(subreddit):
    """gets subscribers from a subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        sub_data = requests.get(url, allow_redirects=False).json()
        return sub_data['data']['subscribers']
    except:
        return 0
