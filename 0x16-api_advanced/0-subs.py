#!/usr/bin/python3
"""
Queries the Reddit API, returns the number of subs for a subreddit or return 0
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    uAgent = {'user-agent' : 'derp'}

    res = requests.get(url, headers= uAgent, allow_redirects=False)
    if res.status_code == 200:
        return res.json().get('data').get('subscribers')
    else:
        return 0
