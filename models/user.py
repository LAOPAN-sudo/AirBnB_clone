#!/usr/bin/python3
"""This class represente some User in our models
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This User class inherit from BaseModel Class
    This class inherit from all methods inside the BaseModel class
    Args:
        :param email(str): The email of the user
        :param password(str): The password of the user
        :param first_name(str): The first_name of the user
        :param last_name(str): The last_name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
