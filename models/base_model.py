#!/usr/bin/python3
"""This class defines all the commmon attributes/methods from others class

Author: @DAVID & @SOULEYTECH
Date: 10/10/2023
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """This class defines all common attributes/methods for other class
    This class does not inherit from another class
    Date:10/10/2023
    """
    def __init__(self, *args, **kwargs):
        """This is the method implemented the constructor

        Args:
            :param args(str): Is a non-keyworded arguments
            :param kwargs(dict): Is a keyworded argument
        """
        size = len(kwargs)
        if size > 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    if key not in ['__class__']:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """This fonction implement the __str__ method
        :return (str): This method return a str representation of instance
        """
        return "[{}] ({}) {}" \
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """This function permit to update an attribute with
        the current datetime
        This method return nothing, but call the new(self)
        from the FileStorage class to add a new instance
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """This function return the dictionary representation
        of an instance of the class
        :return (dict): Return a dictionnary representation of
        an instance
        """
        my_list = self.__dict__
        my_list['__class__'] = self.__class__.__name__
        for key, value in my_list.items():
            if key in ['created_at', 'updated_at']:
                my_list[key] = value.isoformat()
        return my_list
