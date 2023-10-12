#!/usr/bin/python3
"""This is an implementation of the console
Authors: @DAVID & @SOULEY
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = '(hbnb) '

    def emptyline(self):
        pass
    
    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    """BaseModel Interpreter
    """
    def do_create(self, arg):
        if not arg:
            print('** class name missing **')
            return
        if arg not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        if arg in ['BaseModel']:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        args = arg.split()
        if not arg:
            print('** class name missing **')
            return
        if args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        if args[0] in ['BaseModel'] and len(args) < 2:
            print('** instance id missing **')
        else:
            disctall = storage.all()
            if args[1] not in disctall.keys():
                print('** no instance found **')

    """Implementation of helping
    """
    def help_EOF(self):
            print('Quit command to exit the program')

    def help_quit(self):
        print('Quit command to exit the program')

    def help_create(self):
        print('create command create a new BaseModel')
    def help_show(self):
        print('Prints the string representation of an instance based on the class name and id')


if __name__ == '__main__':
    HBNBCommand().cmdloop()