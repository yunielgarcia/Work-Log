import os
import re
import datetime
import csv

OPTIONS_ORDER = ['a', 'b', 'c']
OPTIONS_TEXT = [
    ') Add new entry',
    ') Search in existing entries',
    ') Quit program'
]

SEARCHING_CRITERIA_ORDER = ['a', 'b', 'c', 'd', 'e']
SEARCHING_CRITERIA = [
    ') Exact Date',
    ') Range of Dates',
    ') Exact Search',
    ') Regex Pattern',
    ') Return to Menu',
]


def clean_scr():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_options(order_list, option_list):
    """
    Creates a menu to be printed
    :return: menu (string)
    """
    menu = ''
    for order, text in zip(order_list, option_list):
        menu += (order + text + '\n')
    return menu


def enter_date():
    """
    Receives and validate input data
    :return: date (string)
    """
    valid_data = False
    # used to keep track of the values and change them in other scopes
    input_data = {'date': ''}

    while not valid_data:
        input_data['date'] = input("Date of the task" + "\n" + "Please use DD/MM/YYYY format: ")
        if re.match('\d{2}/\d{2}/\d{4}', input_data['date']):
            try:
                datetime.datetime.strptime(input_data['date'], '%d/%m/%Y')
            except ValueError:
                clean_scr()
                input("Enter a valid date. Press enter to try again.")
            else:
                valid_data = True
                clean_scr()

    return input_data['date']


def enter_title():
    """
    Receives and validate input data
    :return: title (string)
    """
    valid_data = False
    # used to keep track of the values and change them in other scopes
    input_data = {'title': ''}

    while not valid_data:
        input_data['title'] = input("Title of the task: ")
        if re.match('[\w]+', input_data['title']):
            valid_data = True
            clean_scr()

    return input_data['title']


def enter_notes():
    """
    Receives and returns input data
    :return: notes (string)
    """
    return input("Notes (Optional): ")


def enter_time_spent():
    """
    Receives and validate input data
    :return: time_spent (string)
    """
    valid_data = False
    # used to keep track of the values and change them in other scopes
    input_data = {'time_spent': ''}

    while not valid_data:
        input_data['time_spent'] = input("Time spent on task (rounded minutes) : ")
        if re.match('\d+', input_data['time_spent']):
            valid_data = True
            clean_scr()

    return input_data['time_spent']

# SEARCHING FUNCTIONALITY


def enter_searching_date():
    """
    Receives and validate input data
    :return: date (string)
    """
    valid_data = False
    # used to keep track of the values and change them in other scopes
    input_data = {'date': ''}

    while not valid_data:
        input_data['date'] = input("Enter the date" + "\n" + "Please use DD/MM/YYYY format: ")
        if re.match('\d{2}/\d{2}/\d{4}', input_data['date']):
            try:
                datetime.datetime.strptime(input_data['date'], '%d/%m/%Y')
            except ValueError:
                clean_scr()
                input("Enter a valid date. Press enter to try again.")
            else:
                valid_data = True
                clean_scr()
    return input_data['date']


def find_tasks(date_str):
    """
    Opens and reads csv file and collect matching task according to search param
    :param date_str: date to look for
    :return: list of task with match dates
    """
    tasks = []
    try:
        open('log.csv', 'r')
    except IOError:
        print("Couldn't open the file.")
    else:
        with open('log.csv', newline='') as csvfile:
            task_reader = csv.DictReader(csvfile, delimiter=',')
            rows = list(task_reader)
            for row in rows:
                if row['date'] == date_str:
                    tasks.append(row)
            return tasks
