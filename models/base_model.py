#!/usr/bin/python3

"""
"""
import uuid
from datetime import datetime
class BaseModel():
    """
    """
    def __init__(self, *args, **kwargs):
        """
        """
        size = len(kwargs)
        self.id = str(uuid.uuid4()) if size <= 0 else kwargs['id']
        self.created_at = datetime.now() if size <= 0 else datetime.fromisoformat(kwargs['created_at'])
        self.updated_at = datetime.now() if size <= 0 else datetime.fromisoformat(kwargs['updated_at'])
        if size > 0:
            self.name = kwargs['name']
            self.my_number = kwargs['my_number']

    def __str__(self):
        """
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """
        mylist = self.__dict__
        mylist['__class__'] = self.__class__.__name__
        mylist['created_at'] = mylist['created_at'].isoformat()
        mylist['updated_at'] = mylist['updated_at'].isoformat() 
        return mylist
