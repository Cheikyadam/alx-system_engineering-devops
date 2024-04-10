#!/usr/bin/python3
"""alll subs"""
import requests


def number_of_subscribers(subreddit):
    """of subr"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        total = data['data']['subscribers']
        return total
    elif response.status_code == 301 or response.status_code == 302:
        return 0
    else:
        return 0
