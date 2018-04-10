import os
import csv

import utils
from task import Task


def add_entry_data():
    """
    Collects and validates data needed to create a task.
    Creates Task instance.
    Call to save in csv
    """
    task_date = utils.enter_date()
    task_title = utils.enter_title()
    task_time_spent = utils.enter_time_spent()
    task_notes = utils.enter_notes()

    # create instance
    task = Task(task_date, task_title, task_time_spent, task_notes)
    # call to save it
    save_entry(task)


def save_entry(task):
    """
    Saves the task in the csv file
    :param task:
    :return:
    """
    try:
        open('log.csv', 'a')
    except IOError:
        print("Couldn't open the file.")
    else:
        if isinstance(task, Task):
            with open('log.csv', 'a') as csvfile:
                fieldnames = vars(task).keys()
                task_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # only if file is empty write headers
                if os.stat("log.csv").st_size == 0:
                    task_writer.writeheader()

                task_writer.writerow(vars(task))
                utils.clean_scr()
                input("Task added. Press enter to return to the menu")
                utils.clean_scr()
        else:
            print("Couldn't save. Data is corrupted.")


# SEARCHING FUNCTIONALITY


def get_desire_date():
    desire_date = utils.enter_searching_date()
    print(utils.find_tasks(desire_date))
#     todo: getting a match but getting OrderedDict ...see print



def search_tasks():
    """
    Starts the looping over the search actions.
    Once done, it falls back to main menu loop actions
    :return:
    """
    loop_search = True
    while loop_search:
        print("Do you want to search by:" + "\n")
        search_option = input(utils.print_options(utils.SEARCHING_CRITERIA_ORDER, utils.SEARCHING_CRITERIA))
        if search_option == 'e':
            utils.clean_scr()
            loop_search = False
        elif search_option == 'a':
            utils.clean_scr()
            get_desire_date()
        elif search_option == 'b':
            utils.clean_scr()
            search_tasks()
        else:
            print('Please select a letter option.')


# main function
def execute():
    loop = True
    while loop:
        print("\n" + "What would you like to do: " + "\n")
        main_option = input(utils.print_options(utils.OPTIONS_ORDER, utils.OPTIONS_TEXT))
        if main_option == 'c':
            utils.clean_scr()
            print('Thanks.')
            loop = False
        elif main_option == 'a':
            utils.clean_scr()
            add_entry_data()
        elif main_option == 'b':
            utils.clean_scr()
            search_tasks()
        else:
            print('Please select a letter option.')


if __name__ == "__main__":
    execute()
