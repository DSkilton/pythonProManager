class BaseClass:
    project_name = ""
    deadline = ""
    client = ""
    price = ""

    def set_base(self, project_name, deadline, client, price):
        self.project_name = project_name
        self.deadline = deadline
        self.client = client
        self.price = price

    def get_base(self):
        print(self.project_name)
        print(self.deadline)
        print(self.client)
        print(self.price)

