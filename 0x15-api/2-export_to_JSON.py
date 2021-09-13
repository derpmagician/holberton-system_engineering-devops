#!/usr/bin/python3
"""Export data from an API to JSON  format"""
from json import dumps
import requests
from sys import argv

if __name__ == '__main__':
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    api = 'https://jsonplaceholder.typicode.com'
    user_api = '{}/users/{}'.format(api, employee_id)
    todos_user = '{}/todos'.format(user_api)
    filename = '{}.json'.format(employee_id)

    # capture users
    res_user = requests.get(user_api).json()

    # capture tasks
    res_todos = requests.get(todos_user).json()

    # grab data of user
    u_name = res_user.get('name')
    u_username = res_user.get('username')

    # grab number of tasks
    n_tasks = len(res_todos)

    # tasks list
    u_tasks = []
    for todo in res_todos:
        mydata = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": todo.get("username")
            }
        u_tasks.append(mydata)

    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({employee_id: u_tasks}))
