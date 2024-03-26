#!/usr/bin/python3
"""API Gather info"""
import sys
import requests


if __name__ == '__main__':
    url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    try:
        userId = int(sys.argv[1])
        url = f"https://jsonplaceholder.typicode.com/users/{userId}/todos"
        r = requests.get(url)
        r_json = r.json()
        if len(r_json) != 0:
            total = 0
            completed = 0
            for task in r_json:
                total += 1
                if task.get('completed') is True:
                    completed += 1
            url = f"https://jsonplaceholder.typicode.com/users/{userId}"
            r = requests.get(url)
            user = r.json().get('name')
            print(f"Employee {user} is done with tasks({completed}/{total})")
            for task in r_json:
                if task.get('completed') is True:
                    print(f"\t {task.get('title')}")
    except Exception as e:
        print(e)
