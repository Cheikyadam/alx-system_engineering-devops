#!/usr/bin/python3
"""alll subs"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """of subr"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # headers = {'User-Agent':'python-requests/2.22.0'}
    # headers = {'User-Agent': 'MyCustomApp/1.0 (https://www.example.com)'}
    agentChrome = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    agentChrome += 'AppleWebKit/537.36 (KHTML, like Gecko) '
    agentChrome += 'Chrome/97.0.4692.99 Safari/537.36'
    headers = {
                'User-Agent': agentChrome,
                'Accept': 'application/json'
                }

    params = {'limit': 25}

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        for elmnt in data['data']['children']:
            hot_list.append(elmnt['data']['title'])

        after = data['data']['after']

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list[:]
    else:
        return None
