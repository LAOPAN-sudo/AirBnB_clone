#!/usr/bin/python3
"""This class serializes instances to a JSON file and
deserializes JSON file to instances

Authors: @DAVID & @SOULEY
Date: 11/10/2023
"""
import os
import json


class FileStorage():
    """This class serializes instances to a JSON file and deserializes
    JSON file to instances
    This class has two class attributes
    """
    __file_path = os.path.abspath(os.path.dirname("models"))+"/file.json"
    __objects = dict()

    def all(self):
        """This method return all the dictionnary objects
        __objects is a class attributes that content the dictionnary
        representation of each class instance
        """
        return self.__objects

    def new(self, obj):
        """This method permit to sets in __objects
        the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__+"."+obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """Thsi method permit to serializes __objects to
        the JSON file (path: __file_path)
        """
        with open(self.__file_path, mode="w", encoding='utf-8') as file:
            my_obj = self.__objects
            json.dump(my_obj, file)

    def reload(self):
        """This method permit to deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.If the file doesn’t exist, no exception
        should be raised)
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding='utf-8') as file:
                self.__objects = json.loads(json.dumps(json.load(file)))
