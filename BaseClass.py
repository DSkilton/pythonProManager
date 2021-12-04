class BaseClass:
    project_name = ""
    deadline = ""
    client = ""
    price = ""

    def set_details(self, project_name, deadline, client, price):
        self.project_name = project_name
        self.deadline = deadline
        self.client = client
        self.price = price

    def request_info(self):
        self.project_name = input("What is the project name? ")
        self.deadline = input("What is the deadline? ")
        self.client = input("Who is the client? ")
        self.price = input("How much is the quote? ")

    # def get_base(self):
    #     print(self.project_name)
    #     print(self.deadline)
    #     print(self.client)
    #     print(self.price)
    #
