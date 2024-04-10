#!/usr/bin/python3
"""alll subs"""
import requests


def number_of_subscribers(subreddit):
    """of subr"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
        # print("La requête a réussi.")
    elif response.status_code == 301 or response.status_code == 302:
        # print("Redirection détectée mais non suivie.")
        return 0
    else:
        # print("La requête a échoué avec le code de statut:",
        # response.status_code)
        return 0
