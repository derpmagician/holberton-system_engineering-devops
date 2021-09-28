#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests as rq


def recurse(subreddit, hot_list=[], total=''):
    """
    Returns a list with the titles of all hot articles of a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    userAg = {'user-agent': 'derp'}

    payload = {'limit': total}

    res = rq.get(url, headers=userAg, params=payload, allow_redirects=False)
    hot = res.json().get('data', None)

    if res.status_code == 200:
        for post in hot.get('children', []):
            print(post.get('data', {}).get('title', ''))
    else:
        return print('None')
