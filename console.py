#!/usr/bin/python3
""" Defines the HBNB console """
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """ Exits the program."""
        return True

    def emptyline(self):
        """ Overwrites the emptyline method to print nothing """
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
