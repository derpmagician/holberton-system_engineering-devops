#!/usr/bin/python3
"""Export data from an API to CSV format"""
import csv
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
    filename = '{}.csv'.format(employee_id)

    # capture users
    res_user = requests.get(user_api).json()

    # capture tasks
    res_todos = requests.get(todos_user).json()

    # grab data of user
    u_name = res_user.get('name')
    u_username = res_user.get('username')

    # grab number of tasks
    n_tasks = len(res_todos)

    with open(filename, 'w', encoding='utf-8') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for elem in res_todos:
            # grab completion status
            status = elem.get('completed')
            # grab title
            title = elem.get('title')
            my_writer.writerow([employee_id, u_username, status, title])
