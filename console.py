#!/usr/bin/python3
"""the console for the project"""
from models import storage
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}
key_list = []
for i in class_dict:
    key_list.append(i)


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """move to next line when enter is hit"""
        pass

    def do_create(self, arg):
        """creates a new instance and returns its id"""
        if arg in key_list:
            new = eval(arg + "()")
            storage.save()
            print(new.id)
        elif arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")

    def do_show(self, arg):
        """shows the string representation of an instance"""
        arg_passed = arg.split()
        if len(arg_passed) < 2:
            if arg == "":
                print("** class name missing **")
            elif arg_passed[0] not in key_list:
                print("** class doesn't exist **")
            elif arg_passed[0] in key_list:
                print("** instance id missing **")
        elif len(arg_passed) == 2:
            try:
                objs = storage.all()
                set_key = arg_passed[0] + "." + arg_passed[1]
                print(objs[set_key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance"""
        arg_pass = arg.split()
        if len(arg_pass) < 2:
            if arg == "":
                print("** class name missing **")
            elif arg_pass[0] not in key_list:
                print("** class doesn't exist **")
            elif arg_pass[0] in key_list:
                print("** instance id missing **")
        elif len(arg_pass) == 2:
            try:
                set_key = arg_pass[0] + "." + arg_pass[1]
                storage.all().pop(set_key)
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """prints all instance"""
        lines = arg.split()
        ls = []
        obj_dict = storage.all()
        if len(lines) == 1 and lines[0] in key_list:
            for key in obj_dict:
                if obj_dict[key].__class__.__str__() == arg:
                    ls.append(obj_dict[arg].__str__())
            print(ls)
        elif len(arg) == 0:
            for k in obj_dict:
                ls.append(obj_dict[k].__str__())
            print(ls)

    def do_update(self, arg):
        """updates an instance"""
        obj_dict = storage.all()
        list_arg = arg.split()
        if list_arg[0] in key_list:
            for key in obj_dict:
                if obj_dict[key].__class__ == list_arg[0]:
                    obj_dict[list_arg[2]] = list_arg[3]
                    obj_dict.update()
                    storage.save()

    def do_quit(self, line):
        """implementing the quit command"""
        quit()

    def do_EOF(self, line):
        """implementing the EOF"""
        return True

    def do_help(self, arg: str):
        """prints out help options relating to a command"""
        if arg == "quit":
            print("Quit: command to exit the program")
        elif arg == "create":
            print("Create: command to create a new object and return it's ID")
        elif arg == "show":
            print("Show: command to display a string representation of an object")
        else:
            print("""
Documented commands (type help <topic>):
========================================
EOF  help  quit
                """)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
