#!/usr/bin/python3
"""
Class that defines HBNBCommand
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class that defines HBNBCommand
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Exits the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program
        """
        return True

    def emptyline(self):
        """
        Executes nothing
        """
        pass

    def create(self, arg):
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()