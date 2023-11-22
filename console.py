#!venv/bin/python3
"""Console Module"""
import cmd
import shlex
import sys
import models

from models.base_model import BaseModel
from models.blog import Blog
from models.comment import Comment
from models.response import Response
from models.user import User

classes = {"BaseModel": BaseModel, "User": User, "Blog": Blog,
           "Comment": Comment, "Response": Response}


class WalkiThotCMD(cmd.Cmd):
    """Contains the functionality for the WalkiThot console"""

    prompt = '(walkithot) ' if sys.__stdin__.isatty() else ''

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(walkithot)')

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(walkithot) ', end='')
        return stop

    def do_quit(self, command):
        """Method to exit the WalkiThot console"""
        exit()

    def help_quit(self):
        """Prints the help documentation for quit"""
        print("Exits the program with formatting")
        print("You can exit with a simple ctrl-d\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self) -> bool:
        """Overrides the emptyline method of CMD"""
        pass

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except Exception:
                        try:
                            value = float(value)
                        except Exception:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Creates an instance of any Class
        Usage: create <class name> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            attributes = self._key_value_parser(args[1:])
            obj = classes[args[0]](attributes)
        else:
            print("** class doesn't exist **")
            return False
        print(obj.id)
        obj.save()

    def do_show(self, arg):
        """Prints an object as a string based on class and id
        Usage: show <class name> <id>"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an object based on class and id
        Usage: destroy <class name> <id>"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representations of objects
        Usage: all <class name> or all """
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    WalkiThotCMD().cmdloop()
