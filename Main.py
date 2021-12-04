from BaseClass import BaseClass
from website import website
from app import app
from game import game


def test():
    name = website()
    name.project_name = "Project"
    name.deadline = "deadline"
    name.server_name = "192.172.0.0"
    print(name.project_name , name.server_name)


test()
