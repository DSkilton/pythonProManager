from BaseClass import BaseClass


class Game(BaseClass):
    platform = ""
    genre = ""

    def set_details(self, platform, genre):
        self.platform = platform
        self.genre = genre

