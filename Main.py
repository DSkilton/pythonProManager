from BaseClass import BaseClass
from website import Website
from app import App
from game import Game


def menu():
    selection = int(input("Enter a number to proceed\n"
                          "1. New website\t 2. Second Opt\n"
                          "3. New game \t 4. Fourth Opt\n"
                          "5. New app \t\t 6. sixth Opt\n"
                          "7. Seventh Opt \t 8. Exit\n"))

    if selection == 1:
        web = Website()
        web.request_info()
        # web.set_details()


menu()


def new_website():
    name = Website()
    name.project_name = "Project"
    name.deadline = "deadline"
    name.server_name = "192.172.0.0"
    name.get_base()
    print(name.project_name, name.server_name)
