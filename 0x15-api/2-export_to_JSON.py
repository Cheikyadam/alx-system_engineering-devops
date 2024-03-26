#!/usr/bin/python3
"""API Gather info"""
import json
import requests
import sys


if __name__ == '__main__':
    try:
        userId = int(sys.argv[1])
        alltasks = {}
        url = f"https://jsonplaceholder.typicode.com/users/{userId}"
        r = requests.get(url)
        username = r.json().get('username')
        url = f"https://jsonplaceholder.typicode.com/users/{userId}/todos"
        r = requests.get(url)
        allTodos = r.json()
        todos = []
        for task in allTodos:
                todo = {}
                todo['task'] = task.get('title')
                todo['completed'] = task.get('completed')
                todo['username'] = username
                todos.append(todo)
        alltasks[userId] = todos
        filename = f"{userId}.json"
        with open(filename, 'w') as fjson:
            json.dump(alltasks, fjson)
    except Exception as e:
        print(e)
