
'''#!/usr/bin/python3'''
'''display standard output of todo list'''
import requests
import csv
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
    '''count tasks'''
    with open(av[1] + '.csv', 'w') as csvfile:
        taskwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos_json:
            if task['userId'] == int(av[1]):
                taskwriter.writerow(
                    [av[1], employee_name, task['completed'], task['title']])
