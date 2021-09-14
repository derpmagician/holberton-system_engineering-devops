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

    main_dict = {}
    for user in res_user:
        username = user['username']
        task_list = []
        for todos in res_todos:
            if todos['userId'] == user['id']:
                di = {}
                di['username'] = username
                di['task'] = todos['title']
                di['completed'] = todos['completed']
                task_list.append(di)
        main_dict[user['id']] = task_list

    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(main_dict, f)
    """
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps(main_dict))
