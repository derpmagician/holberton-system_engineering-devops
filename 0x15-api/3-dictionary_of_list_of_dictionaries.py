#!/usr/bin/python3
"""Export data from an API to JSON  format"""
from json import dumps
import requests

if __name__ == '__main__':

    api = 'https://jsonplaceholder.typicode.com'
    users_api = '{}/users'.format(api)
    todos_api = '{}/todos'.format(api)
    filename = 'todo_all_employees.json'

    res_user = requests.get(users_api).json()
    res_todos = requests.get(todos_api).json()

    """
    for user in res_user:
        username = user['username']
        for todo in res_todos:
            if todo['userId'] == user['id']:
                # mylist = []
                print(todo['userId'])
    """

    dicx = {}
    for user in res_user:
        username = user['username']
        ll = []
        for todos in res_todos:
            if todos['userId'] == user['id']:
                di = {}
                di['username'] = username
                di['task'] = todos['title']
                di['completed'] = todos['completed']
                ll.append(di)
        dicx[user['id']] = ll

    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dicx, f)
    """
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps(dicx))
