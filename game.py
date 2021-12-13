from ProjectBasics import ProjectBasics


class Game(ProjectBasics):
    platform = ""
    genre = ""

    def request_info(self):
        base = ProjectBasics()
        base.request_info()
        self.set_details()

    def set_details(self):
        self.platform = input("Which platform? ")
        self.genre = input("What genre? ")
