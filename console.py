#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class defines the entry point of the command interpreter
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity, "Place": Place,
        "Review": Review
        }

    def do_create(self, line):
        """
        Create command to create a new instance
        """
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Show command to show an instance
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Destroy command to delete an instance
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """
        All command to print all instances
        """
        args = line.split()
        if not args:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([
                str(obj) for key, obj in storage.all().items()
                if key.startswith(f"{args[0]}.")
            ])

    def do_update(self, line):
        """
        Update command to update an instance
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], args[3])
        obj.save()

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        print("")
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn’t execute anything
        """
        pass

    def default(self, line):
        """
        Default behavior for cmd module when input is invalid
        """
        if '.' not in line:
            print("*** Unknown syntax: {}".format(line))
            return
        segment = line.split('.')
        class_name = segment[0]
        method_name = segment[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if method_name == "all()":
            self.do_all(class_name)
        elif method_name == "count()":
            self.do_count(class_name)
        elif method_name.startswith("show(") and method_name.endswith(")"):
            method_name = method_name[len("show("):-1].strip()
            if method_name.startswith('"') and method_name.endswith('"'):
                method_name = method_name[1:-1]
            self.do_show(class_name + " " + method_name)
            return
        elif method_name.startswith("destroy(") and method_name.endswith(")"):
            method_name = method_name[len("destroy("):-1].strip()
            if method_name.startswith('"') and method_name.endswith('"'):
                method_name = method_name[1:-1]
            self.do_destroy(class_name + " " + method_name)
            return
        elif method_name.startswith("update(") and method_name.endswith(")"):
            method_name = method_name[len("update("):-1].strip()
            if method_name.startswith('"') and method_name.endswith('"'):
                method_name = method_name[1:-1]
            self.do_update(class_name + " " + segment[1] + " " + segment[2])
        else:
            print("*** Unknown syntax: {}".format(line))
            return

    def do_count(self, line):
        """
        Count command to count the number of instances of a class
        """
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            count = sum(
                1 for key in storage.all()
                if key.startswith(f"{args[0]}.")
            )
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
