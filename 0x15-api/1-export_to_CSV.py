#!/usr/bin/python3
"""Export data from an API to CSV format.
"""
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
