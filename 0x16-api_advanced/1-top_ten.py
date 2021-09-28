#!/usr/bin/python3
"""
Queries the Reddit API, prints titles of the first 10 hot posts in a subreddit
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
    body = res.json().get('data')

    if res.status_code == 200:
        for post in body.get('children'):
            print(post.get('data', {}).get('title', ''))
    else:
        return print('None')

