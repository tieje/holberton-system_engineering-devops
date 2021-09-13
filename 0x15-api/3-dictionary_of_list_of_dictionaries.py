#!/usr/bin/python3
'''display standard output of todo list'''
from json import dump
import requests
from urllib.parse import urljoin
from sys import argv as av

if __name__ == "__main__":
    '''paths'''
    main_path = 'https://jsonplaceholder.typicode.com/'
    users_path = urljoin(main_path, '/users')
    todos_path = urljoin(main_path, '/todos')
    '''json'''
    users_json = requests.get(users_path).json()
    todos_json = requests.get(todos_path).json()
    '''extract reusable data'''
    name_list = []
    task_dict = {}
    for user in users_json:
        task_dict[user['id']] = []
        name_list.append(user['username'])
    '''put task in json format'''
    for task in todos_json:
        temp_dict = {}
        temp_dict['username'] = name_list[task['userId'] - 1]
        temp_dict['task'] = task['title']
        temp_dict['completed'] = task['completed']
        task_dict[task['userId']].append(temp_dict)

    with open('todo_all_employees.json', 'w') as file:
        dump(task_dict, file)
