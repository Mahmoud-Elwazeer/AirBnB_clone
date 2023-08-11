#!/usr/bin/env python3
"""called console that contains the entry point of the command interpreter"""
import cmd
import os
from models.all_models import our_models
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
        elif line not in our_models.keys():
            print("** class doesn't exist **")
        else:
            storage.reload()
            self.my_model = our_models[line]()
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
        elif args[0] not in our_models.keys():
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

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        Ex: all <ClassName> or all
        """
        out_all = []
        if not line:
            data = storage.all()
            for key, value in data.items():
                out_all.append(str(data[key]))
            print(out_all)
        elif line not in our_models.keys():
            print("** class doesn't exist **")
        else:
            data = storage.all()
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                if line == class_name:
                    out_all.append(str(data[key]))
                else:
                    pass
            print(out_all)

    def do_destroy(self, line):
        """ deletes an instance based on the class name and id.
        Ex: destroy <ClassName> <id>
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in our_models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            my_dict = storage.all()
            my_key = args[0] + '.' + args[1]
            if my_key in my_dict.keys():
                del my_dict[my_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, line):
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in our_models.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            my_dict = storage.all()
            my_key = args[0] + '.' + args[1]
            if my_key in my_dict.keys():
                setattr(my_dict[my_key], args[2], args[3])
                storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
