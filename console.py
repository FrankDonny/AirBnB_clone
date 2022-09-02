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
            new = eval(arg + "()")  # arg()
            storage.save()
            print(new.id)
        elif arg == "":
            print("** class name missing **")
        elif arg not in key_list:
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
                if obj_dict[key].__class__.__name__ == arg:
                    ls.append(obj_dict[key].__str__())
            print(ls)
        elif len(arg) == 0:
            for k in obj_dict:
                ls.append(obj_dict[k].__str__())
            print(ls)

    def do_update(self, arg):
        """updates an instance"""
        obj_dict = storage.all()
        if len(arg.split()) == 4:
            args = arg.split()
            obj = args[0] + "." + args[1]
            new_attr = args[2]
            new_attr_val = args[3]
            for k, v in obj_dict.items():
                if k == obj:
                    setattr(storage.all()[k], new_attr,
                            new_attr_val.strip("\""))
                    # if "." in new_attr_val.strip("\"") and any([x.isdigit() for x in new_attr_val]):
                    #     new_attr_val = float(new_attr_val)
                    # elif new_attr_val.isdigit():
                    #     new_attr_val = int(new_attr_val)
                    storage.all()[k].save()
        elif len(arg.split()) == 0:
            print("** class name missing **")
        if len(arg.split()) == 1:
            args = arg.split()
            if args[0] not in key_list:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        if len(arg.split()) == 2:
            args = arg.split()
            if (args[0] + "." + args[1]) not in storage.all():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(arg.split()) == 3:
            args = arg.split()
            if (args[0] + "." + args[1]) in storage.all():
                print("** value missing **")
        elif len(arg.split()) > 4:
            pass

    # def default(self, arg):
    #     args = arg.split(".")
    #     ct = 1
    #     objs = storage.all()
    #     if args[1] == "count()" and args[0] in key_list:
    #         for key in objs:
    #             ky = key.split()
    #             if ky[0] == args[0]:
    #                 ct += 1
    #                 print(ct)

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
            print("Show: command to display a string representation"
                  "of an object")
        else:
            print("""

Documented commands (type help <topic>):
========================================
EOF  help  quit
""")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
