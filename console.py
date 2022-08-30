#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    file = None

    # def do_help(self, arg: str):
    #     print("""
    #     Welcome to the help menu
    #     create: to create
    #     quit: to quit the console
    #     """)

    def do_quit(self, line):
        quit()

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
