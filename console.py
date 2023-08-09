#!/usr/bin/env python3
"""called console that contains the entry point of the command interpreter"""
import cmd
import os

class HBNBCommand(cmd.Cmd):
    """ simple command processor Example"""

    prompt = '(hbnb) '

    def do_shell(self, line):
        output = os.popen(line).read()
        print(output)

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
