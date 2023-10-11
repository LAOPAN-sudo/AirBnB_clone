#!/usr/bin/python3
"""
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    """
    def __init__(self, *args, **kwargs):
        """
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
        """
        """
        return "[{}] ({}) {}" \
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        """
        my_list = self.__dict__
        my_list['__class__'] = self.__class__.__name__
        for key, value in my_list.items():
            if key in ['created_at', 'updated_at']:
                my_list[key] = value.isoformat()
        return my_list
