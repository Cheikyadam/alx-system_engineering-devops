#!/usr/bin/python3
"""API Gather info"""
import json
import requests
import sys


if __name__ == '__main__':
    try:
        allemployees = {}
        url = f"https://jsonplaceholder.typicode.com/users/"
        r = requests.get(url)
        allUsers = r.json()
        for user in allUsers:
            userId = user.get('id')
            url = f"https://jsonplaceholder.typicode.com/users/{userId}/todos"
            r = requests.get(url)
            allTodos = r.json()
            todos = []
            for task in allTodos:
                todo = {}
                todo['username'] = user.get('username')
                todo['task'] = task.get('title')
                todo['completed'] = task.get('completed')
                todos.append(todo)
            allemployees[userId] = todos
        filename = "todo_all_employees.json"
        with open(filename, 'w') as fjson:
            json.dump(allemployees, fjson)
    except Exception as e:
        print(e)
