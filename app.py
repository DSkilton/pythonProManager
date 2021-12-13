from ProjectBasics import ProjectBasics


class App(ProjectBasics):
    type = ""

    def request_info(self):
        base = ProjectBasics()
        base.request_info()
        self.set_details()

    def set_details(self):
        self.type = input("What type of app? ")
