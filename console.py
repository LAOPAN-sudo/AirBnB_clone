#!/usr/bin/python3
"""This is an implementation of the console
Authors: @DAVID & @SOULEY
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the class that implement the cmd module
    to do some console
    """
    prompt = '(hbnb) '

    instances = []
    def emptyline(self):
        """This method permit to override the default emptyline behavior
        """
        pass

    def do_quit(self, arg):
        """Implement the quit method
        """
        return True

    def do_EOF(self, arg):
        """This command permit to exit the console
        """
        return True

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
        if arg not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        if arg in ['BaseModel']:
            my_model = BaseModel()
            my_model.save()
            self.instances.append(my_model)
            print(my_model.id)

    def do_show(self, arg):
        """This command permit to show the content of an instance
        of a BaseModel
        Args:
            This method take a argument after the command
        :param arg(str): split it in list of string
        """
        args = arg.split()
        if not arg:
            print('** class name missing **')
            return
        if args[0] not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        if args[0] in ['BaseModel'] and len(args) < 2:
            print('** instance id missing **')
            return
        if len(self.instances) > 0:
            for item in self.instances:
                if item.id == args[1]:
                    print(item)
                    return
            print('** no instance found **')
            return
        else:
            print('** no instance found **')
            return


    """Implementation of helping
    """
    def help_EOF(self):
        """Give the documentation from the EOF command
        """
        print('Quit command to exit the program')

    def help_quit(self):
        """Give the doc of the quit command
        """
        print('Quit command to exit the program')

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
