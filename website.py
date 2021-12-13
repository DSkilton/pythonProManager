from ProjectBasics import ProjectBasics


class Website(ProjectBasics):
    server_name = ""
    number_of_pages = ""

    def request_info(self):
        base = ProjectBasics()
        base.request_info()
        self.set_details()

    def set_details(self):
        self.server_name = input("What is the server add? ")
        self.number_of_pages = input("How many pages? ")

