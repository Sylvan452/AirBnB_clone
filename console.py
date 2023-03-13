#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """ class for the console"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """indicates end of line, exits on ctrl D"""
        print()
        return True

    def do_quit(self, line):
        """EXits on quit """
        return True

    def emptyline(self):
        """executes when an empty line is passed"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
