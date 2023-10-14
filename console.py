#!/usr/bin/python3
"""This is an implementation of the console
Authors: @DAVID & @SOULEY
"""
import cmd
import re
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the class that implement the cmd module
    to do some console
    """
    prompt = '(hbnb) '
    classes = {
        'BaseModel', 'Amenity', 'City', 'Place', 'Review', 'State', 'User'
        }

    def emptyline(self):
        """This method permit to override the default emptyline behavior
        """
        pass

    def do_quit(self, arg):
        """Implement the quit method
        """
        return True

    do_EOF = do_quit

    """BaseModel Interpreter
    """
    def do_create(self, arg):
        """This command permit to create a new instance of BaseModel
        Args:
            This command take one argument on parameter
            :param arg(string): The string after the command
        """
        if not arg:
            print('** class name missing **')
            return
        if arg in self.classes:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
            return
        print("** class doesn't exist **")
        return

    def do_show(self, arg):
        """This command permit to create a new instance of BaseModel
        Args:
            This command take one argument on parameter
            :param arg(string): The string after the command
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if f"{args[0]}.{args[1]}" == obj_id:
                obj = all_objs[obj_id]
                print(obj)
                return
        print("** no instance found **")
        return

    def do_all(self, arg):
        """This command permit to create a new instance of BaseModel
        Args:
            This command take one argument on parameter
            :param arg(string): The string after the command
        """
        if not arg:
            all_objs = storage.all()
            list_all = []
            for obj_id in all_objs.keys():
                obj = all_objs[obj_id]
                list_all.append(str(obj))
            print(list_all)
            return
        if arg in self.classes:
            all_objs = storage.all()
            list_model = []
            for obj_id in all_objs.keys():
                if re.search(arg, obj_id):
                    obj = all_objs[obj_id]
                    list_model.append(str(obj))
            if len(list_model) > 0:
                print(list_model)
            return
        print("** class doesn't exist **")
        return

    def do_count(self, arg):
        """This command permit to create a new instance of BaseModel
        Args:
            This command take one argument on parameter
            :param arg(string): The string after the command
        """
        if arg in self.classes:
            all_objs = storage.all()
            nb_instance = 0
            for obj_id in all_objs.keys():
                if re.search(arg, obj_id):
                    nb_instance = nb_instance + 1
            print(nb_instance)
            return
        print("** class doesn't exist **")
        return


    def do_destroy(self, arg):
        """This command permit to delete a new instance in the models
        Args:
            This command take one argument on parameter
            :param arg(string): The string after the command
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if f"{args[0]}.{args[1]}" == obj_id:
                del all_objs[obj_id]
                storage.save()
                return
        print("** no instance found **")
        return

    def do_update(self, arg):
        """This command permit to update only one attribute of an instance
        Args:
            This command take one argument on parameter
            :param arg(string): The string after the command
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** id instance missing **")
            return
        b = True
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if f"{args[0]}.{args[1]}" == obj_id:
                b = False
        if b:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = all_objs[f"{args[0]}.{args[1]}"]
        if args[2] in obj.__class__.__dict__.keys():
            if args[2] not in {'id', 'created_at', 'updated_at'}:
                attr_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = attr_type(args[3])
        else:
            if obj.__class__.__name__ == 'BaseModel':
                obj.__dict__[args[2]] = args[3]
        storage.save()
        return

    """Implementation of helping
    """
    def help_quit(self):
        """Give the doc of the quit command
        """
        print('Quit command to exit the program')

    help_EOF = help_quit

    def help_create(self):
        """Give the doc of the create command
        """
        print('create command create a new BaseModel')

    def help_show(self):
        """Give the doc of the show command
        """
        print('Prints the string representation of an \
                instance based on the class name and id')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
