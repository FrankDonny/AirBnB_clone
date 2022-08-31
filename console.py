#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        if arg == "BaseModel":
            new = BaseModel()
            print(new.id)
        elif arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")

    def do_show(self, arg):
        arg_passed = arg.split()
        if len(arg_passed) < 2:
            if arg == "":
                print("** class name missing **")
            elif arg_passed[0] != "BaseModel":
                print("** class doesn't exist **")
            elif arg_passed[0] == "BaseModel":
                print("** instance id missing **")
        elif len(arg_passed) == 2:
            try:
                objs = storage.all()
                set_key = arg_passed[0] + "." + arg_passed[1]
                print(objs[set_key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        arg_pass = arg.split()
        if len(arg_pass) < 2:
            if arg == "":
                print("** class name missing **")
            elif arg_pass[0] != "BaseModel":
                print("** class doesn't exist **")
            elif arg_pass[0] == "BaseModel":
                print("** instance id missing **")
        elif len(arg_pass) == 2:
            try:
                set_key = arg_pass[0] + "." + arg_pass[1]
                # storage.save()
            except KeyError:
                print("** no instance found **")

    def do_quit(self, line):
        quit()

    def do_EOF(self, line):
        return True

    def do_help(self, arg: str):
        if arg == "quit":
            print("Quit command to exit the program")
        elif arg == "create":
            print("Create command to create a new object and return it's ID")
        elif arg == "show":
            print("Show command to display a string representation of an object")
        else:
            print("""
Documented commands (type help <topic>):
========================================
EOF  help  quit
                """)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
