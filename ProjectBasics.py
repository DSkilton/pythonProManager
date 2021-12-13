import Main


def correct_details(correct):
    if correct == "yes":
        print("Returning to Main Menu")
        Main.menu()


def next_option():
    input("What would you like to do now? \n"
          "1. Main menu"
          "2. Exit")


class ProjectBasics:
    project_name = ""
    deadline = ""
    client = ""
    price = ""

    def set_details(self):
        pass

    def request_info(self):
        self.project_name = input("What is the project name? ")
        self.deadline = input("What is the deadline? ")
        self.client = input("Who is the client? ")
        self.price = input("How much is the quote? ")

    def confirm_project_info(self):
        print("Is the following correct "
              "Project name:\t" + self.project_name + "\n"
              "Deadline:\t" + self.deadline + "\n"
              "Client:\t" + self.client + "\n"
              "Price:\t" + self.price + "\n")
        correct = input(str("Are the details correct?")).lower()
        correct_details(correct)
