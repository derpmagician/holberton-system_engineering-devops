#!/usr/bin/python3
"""
Queries the Reddit API
"""
import requests as rq


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list with the titles of all hot articles of a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}" \
          .format(subreddit, after)

    userAg = {'user-agent': 'derp'}

    payload = {'limit': after}

    res = rq.get(url, headers=userAg, params=payload, allow_redirects=False)
    # hot = res.json().get('data', after)

    if res.status_code == 200:
        top_posts = res.json()
        key = top_posts['data']['after']
        parent = top_posts['data']['children']
        for obj in parent:
            hot_list.append(obj['data']['title'])
        if key is not None:
            recurse(subreddit, hot_list, key)
        return hot_list
    else:
        return None
