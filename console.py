#!/usr/bin/python3
""" Defines the HBNB console """
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """ Exits the program."""
        return True

    def emptyline(self):
        """ Overwrites the emptyline method to print nothing """
        return False

    def do_create(self, arg):
        """
        Creates a new class instance, saes it and print its id.
        """
        if not len(arg):
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            print(new.id)
            new.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id
        """
        if not len(arg):
            print("** class name missing **")
            return
        lines = split(arg)
        if lines[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(lines) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = lines[0] + '.' + lines[1]
        if key in objs:
            print(objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class and id and saves the change
        """
        if not len(arg):
            print("** class name missing **")
            return
        lines = arg.split(" ")
        if lines[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(lines) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = lines[0] + '.' + lines[1]
        if key in objs:
            del objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        if not len(arg):
            print([obj for obj in storage.all().values()])

        line = split(arg)
        if line[0] not in self.__classes:
            print("** class doesn't exist **")

        for obj in storage.all().values():
            if line[0] == type(obj).__name__:
                print(obj)

    def do_update(self, arg):
        """
        Update an instance based on the class name, id, attribute & value
        """
        if not len(arg):
            print("** class name missing **")
            return
        line = split(arg, " ")

        if line[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        objs = storage.all()
        key = line[0] + '.' + line[1]

        if key not in objs:
            print("** no instance found **")
            return
        if len(line) < 3:
            print("** attribute name missing **")
            return
        if len(line) < 4:
            print("** value missing **")
            return

        value = objs[key]
        try:
            value.__dict__[line[2]] = eval(line[3])
        except Exception:
            value.__dict__[line[2]] = line[3]
            value.save()

    def default(self, arg):
        """ Default behavior for invalid input"""
        kwargs = {
            "all": self.do_all,
        }
        match = re.search(r"\.", arg)
        if match:
            args = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match:
                command = [args[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in kwargs.keys():
                    method = "{} {}".format(args[0], command[1])
                    return kwargs[command[0]](method)

        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
