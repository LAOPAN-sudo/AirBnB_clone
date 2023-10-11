#!/usr/bin/python3

"""
This script defines a class `BaseModel`
with common attributes and methods for other classes.
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    This is the BaseModel class.

    Attributes:
        id (str): Unique ID for the instance.
        created_at (datetime): The datetime when the instance is created.
        updated_at (datetime): The datetime when the instance is last updated.
        name (str): Name attribute (if provided).
        my_number (int): My number attribute (if provided).
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        If keyword arguments are provided,
            the attributes are initialized with these values.
        If no keyword arguments are provided,
            the attributes are initialized with default values.
        """
        size = len(kwargs)
        if size > 0:
            for key, value in kwargs.items():
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A formatted string with
                class name, ID, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing
                all instance attributes and class name.
        """
        mylist = self.__dict__
        mylist['__class__'] = self.__class__.__name__
        mylist['created_at'] = mylist['created_at'].isoformat()
        mylist['updated_at'] = mylist['updated_at'].isoformat()
        return mylist
