#!/usr/bin/python3
"""API Gather info"""
import csv
import requests
import sys


if __name__ == '__main__':
    try:
        userId = int(sys.argv[1])
        url = f"https://jsonplaceholder.typicode.com/users/{userId}/todos"
        r = requests.get(url)
        r_json = r.json()
        url = f"https://jsonplaceholder.typicode.com/users/{userId}"
        r = requests.get(url)
        user = r.json().get('name')
        filename = f"{userId}.csv"
        with open(filename, mode='w', newline='') as fcsv:
            writer = csv.writer(fcsv)
            for task in r_json:
                line = []
                line.append(userId)
                line.append(user)
                line.append(task.get('completed'))
                line.append(task.get('title'))
                writer.writerow(line)
    except Exception as e:
        print(e)
