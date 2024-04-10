#!/usr/bin/python3
"""alll subs"""
import requests


def number_of_subscribers(subreddit):
    """of subr"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    agentChrome = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    agentChrome += 'AppleWebKit/537.36 (KHTML, like Gecko) '
    agentChrome += 'Chrome/97.0.4692.99 Safari/537.36'
    headers = {
                'User-Agent': agentChrome,
                'Accept': 'application/json'
                }
    params = {'limit': 1}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        total = data['data']['subscribers']
        return total
    elif response.status_code == 301 or response.status_code == 302:
        print(response.status_code)
        return 0
    else:
        print(response.status_code)
        return 0
