#!/usr/bin/python3
'''display standard output of todo list'''
from json import dump
import requests
from urllib.parse import urljoin
from sys import argv as av

if __name__ == "__main__":
    '''paths'''
    main_path = 'https://jsonplaceholder.typicode.com/'
    user_path = urljoin(main_path, '/users/' + av[1])
    todos_path = urljoin(main_path, '/todos')
    '''json'''
    user_json = requests.get(user_path).json()
    todos_json = requests.get(todos_path).json()
    '''extract reusable data'''
    employee_name = user_json['name']
    task_dict = {}
    task_dict[av[1]] = []
    '''put task in json format'''
    for task in todos_json:
        if task['userId'] == int(av[1]):
            temp_dict = {}
            temp_dict['task'] = task['title']
            temp_dict['completed'] = task['completed']
            temp_dict['username'] = employee_name
            task_dict[av[1]].append(temp_dict)

    with open('{}.json'.format(av[1]), 'w') as file:
        dump(task_dict, file)
