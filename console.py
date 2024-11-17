#!/usr/bin/python3
"""
Entry point for the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB application.
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program with EOF (Ctrl+D).
        Usage: EOF
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """Creates a new basemodel and saves it, and prints it's id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in classes:
            print("** class doesn't exist **")
            return
        instance = classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances."""
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        result = []
        for key, obj in objects.items():
            if not arg or key.startswith(arg + "."):
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Updates an instance by adding or updating an attribute."""
        args = arg.split(maxsplit=3)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if attr_name not in ("id", "created_at", "updated_at"):
            try:
                # Attempt to cast the value to int or float if possible
                if '.' in attr_value:
                    attr_value = float(attr_value)
                else:
                    attr_value = int(attr_value)
            except ValueError:
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()
    def default(self, line):
        """
        Handle commands in the format <class name>.all().
        """
        if '.' not in line:
            print("*** Unknown syntax:", line)
            return
        
        # Split the input into class name and command
        try:
            class_name, command = line.split('.')
            command, _ = command.split('(', 1)  # Get the command part (e.g., "all")
        except ValueError:
            print("*** Unknown syntax:", line)
            return

        # Check if the class exists
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if command == "all":
            # Retrieve all instances of the specified class
            objects = storage.all()
            result = [
                str(obj) for key, obj in objects.items() if key.startswith(f"{class_name}.")
            ]
            print(result)
        else:
            print("*** Unknown syntax:", line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
