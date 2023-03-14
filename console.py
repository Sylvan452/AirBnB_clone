#!/usr/bin/python3
"""Console for Airbnb clone """
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """ Entry into the console"""
    prompt = "(hbnb)"
    classes = {"BaseModel", "Amenity", "User", "Place", "Review", "State",
               "City"}

    def do_EOF(self, line):
        """indicates end of line, exits on ctrl D"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """executes when an empty line is passed"""
        pass

    def do_create(self, line):
        """creates an instance of BaseModel, line contains the class"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            '''evaluate the string in line to a funtion object'''
            instance = eval(line)()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        '''prints the string representation of an instance: name.id'''
        if len(args) == 0:
            print("** class name missing **")
            return
        args = args.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[1]:
            name = "{}.{}".format(args[0], args[1])
            if name not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[name])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
