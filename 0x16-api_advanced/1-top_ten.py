#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests as rq


def top_ten(subreddit):
    """
    Prints titles of the first 10 hot posts in a subredditt.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    userAg = {'user-agent': 'derp'}

    payload = {'limit': '10'}

    res = rq.get(url, headers=userAg, params=payload, allow_redirects=False)
    hot = res.json().get('data', None)

    if res.status_code == 200:
        for post in hot.get('children'):
            print(post.get('data').get('title'))
    else:
        return print('None')
