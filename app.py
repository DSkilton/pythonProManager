from BaseClass import BaseClass


class App(BaseClass):
    type = ""

    def request_info(self):
        base = BaseClass()
        base.request_info()
        self.set_details()

    def set_details(self):
        self.type = input("What type of app? ")
