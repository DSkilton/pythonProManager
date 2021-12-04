from BaseClass import BaseClass


class Game(BaseClass):
    platform = ""
    genre = ""

    def request_info(self):
        base = BaseClass()
        base.request_info()
        self.set_details()

    def set_details(self):
        self.platform = input("Which platform? ")
        self.genre = input("What genre? ")
