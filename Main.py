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
    elif selection == 2:
        app = App()
        app.request_info()
    elif selection == 3:
        game = Game()
        game.request_info()


menu()
