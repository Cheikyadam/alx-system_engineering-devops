#!/usr/bin/python3
"""alll subs"""
import requests


def number_of_subscribers(subreddit):
    """of subr"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    #headers = {'User-Agent': 'python-requests/2.22.0'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    #response = requests.get(url, headers=headers)
    # allow_redirects=False)
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
