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
import os


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
        """creates an instance of BaseModel
           Usage: create <class_name>
        """
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

    def do_destroy(self, args):
        """deletes an instance based on class name and id"""
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
            instance = "{}.{}".format(args[0], args[1])
            if instance not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[instance]
                storage.save()

    def do_all(self, args):
        '''prints all str representation of an instance based on class name'''
        all_list = []
        if len(args) == 0:
            for obj in storage.all().values():
                all_list.append(str(obj))
            print(all_list)
            return
        args = args.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                if args[0] in key:
                    all_list.append(str(obj))
            print(all_list)

    def do_update(self, args):
        """updates an instance attribute"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3].strip("'")
            arg3 = arg3.strip('"')
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
            return
        else:
            print("** value missing **")
            return

    def do_clear(self, args):
        '''Behaves like clear in shell'''
        os.system('clear')

    def do_count(self, args):
        '''counts the number of class an instance occurs'''
        if args in self.classes:
            count = 0
            for key, val in storage.all().items():
                if args in key:
                    count += 1
            print(count)
            return
        else:
            print("** class doesn't exist **")
            return

    def default(self, args):
        '''Accept class_name and method; e.g: User.count()'''
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(args))
            return
        args = args.split('.')
        class_arg = args[0]
        try:
            args = args[1].split('(')  # resets args to start form args[1]
            command = args[0]  # e.g - count, all

            if command == 'all':
                HBNBCommand.do_all(self, class_arg)

            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)

            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)

            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)

            elif command == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip('"')
                id_arg = id_arg.strip("'")
                name_arg = args[1].strip(',')
                name_arg = name_arg.strip("'").strip('"')
                name_arg = name_arg.strip(' ')
                val_arg = args[2].strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)

            else:
                print("*** Unknown syntax: {}".format(args))
        except IndexError:
            print("*** Unknown syntax: {}".format(args))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
