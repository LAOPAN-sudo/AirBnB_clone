#!/usr/bin/python3
"""
"""
import os
import json


class FileStorage():
    """
    """
    __file_path = os.path.abspath(os.path.dirname("models"))+"/file.json"
    __objects = dict()

    def all(self):
        """
        """
        return self.__objects

    def new(self, obj):
        """
        """
        key = obj.__class__.__name__+"."+obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        """
        with open(self.__file_path, mode="w", encoding='utf-8') as file:
            """
            """
            my_obj = self.__objects
            json.dump(my_obj, file)

    def reload(self):
        """
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as file:
                """
                """
                self.__objects = json.loads(json.dumps(json.load(file)))
