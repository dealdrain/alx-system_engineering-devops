#!/usr/bin/python3
"""
function that queries the Reddit API
returns the number of subscribers
"""


import requests

BASE_URL = 'https://reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    """
    Getting count of reddit subs
    """
    headers = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(BASE_URL.format(subreddit),
                            headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)
