#!/usr/bin/python3
'''display standard output of todo list'''
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
    total_tasks = 0
    tasks_completed = 0
    task_titles = []
    '''count tasks'''
    for task in todos_json:
        if task['userId'] == int(av[1]):
            if task['completed'] is True:
                tasks_completed += 1
            total_tasks += 1
            task_titles.append(task['title'])
    print('Employee {} is done with tasks {}/{}'
          .format(employee_name, tasks_completed, total_tasks))
    for title in task_titles:
        print('\t ' + title)
