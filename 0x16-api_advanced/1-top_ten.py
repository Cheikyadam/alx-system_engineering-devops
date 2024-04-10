#!/usr/bin/python3
"""alll subs"""
import requests


def top_ten(subreddit):
    """of subr"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # headers = {'User-Agent':'python-requests/2.22.0'}
    agentChrome = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    agentChrome += 'AppleWebKit/537.36 (KHTML, like Gecko) '
    agentChrome += 'Chrome/97.0.4692.99 Safari/537.36'
    headers = {
                'User-Agent': agentChrome,
                'Accept': 'application/json'
                }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for i in range(0, 10):
            title = data['data']['children'][i]['data']['title']
            print(title)
    elif response.status_code == 301 or response.status_code == 302:
        print(None)
        # return 0
    else:
        print(None)
        # return 0
