from BaseClass import BaseClass


class website(BaseClass):
    server_name = ""
    number_of_pages = ""

    def set_web_details(self, server_name, num_of_pages):
        self.server_name = server_name
        self.number_of_pages = num_of_pages
