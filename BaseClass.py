class BaseClass:
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

