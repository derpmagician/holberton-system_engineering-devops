#!/usr/bin/python3
'''get employeed information with ID'''

import requests
from  sys import argv

if __name__ == '__main__':
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()
    api = 'https://jsonplaceholder.typicode.com'
    user_api = '{}/users/{}'.format(api, employee_id)
    todos_user = '{}/todos'.format(user_api)

    # capture users
    res_user = requests.get(user_api).json()

    # capture tasks
    res_todos = requests.get(todos_user).json()

    # grab name of user
    u_name = res_user.get('name')

    # grab number of tasks
    n_tasks = len(res_todos)

    # completed tasks
    completed_tasks = []
    for item in res_todos:
        if item['completed'] is True:
            completed_tasks.append(item)

    #count completed tasks
    sum_completed = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(u_name, sum_completed, n_tasks))

    for item in res_todos:
        if item.get('completed') is True:
            print('\t', item.get('title'))
