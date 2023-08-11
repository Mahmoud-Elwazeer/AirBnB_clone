#!/usr/bin/env python3
"""called console that contains the entry point of the command interpreter"""
import cmd
import os
from models.all_models import models
from models import storage


class HBNBCommand(cmd.Cmd):
    """ simple command processor Example"""

    prompt = '(hbnb) '

    def do_shell(self, line):
        """excute shell command type shell[command] or ![command]
        """
        output = os.popen(line).read()
        print(output)

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """overrides for original func"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """creates new instace as save it to json file
        """
        if not line:
            print("** class name missing **")
        elif line not in models.keys():
            print("** class doesn't exist **")
        else:
            storage.reload()
            self.my_model = models[line]()
            self.my_model.save()
            print(self.my_model.id)

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id.
        Ex: show <ClassName> <id>
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            my_dict = storage.all()
            my_key = args[0] + '.' + args[1]
            if my_key in my_dict.keys():
                print(my_dict[my_key])
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
