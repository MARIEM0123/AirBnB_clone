#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

def parse(arg):
    cb = re.search(r"\{(.*?)\}", arg)
    brk = re.search(r"\[(.*?)\]", arg)
    if cb is None:
        if brk is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lx = split(arg[:brk.span()[0]])
            nl = [i.strip(",") for i in lx]
            nl.append(brk.group())
            return nl
    else:
        lx = split(arg[:cb.span()[0]])
        nl = [i.strip(",") for i in lx]
        nl.append(cb.group())
        return nl

class HBNBCommand(cmd.Cmd):
    """The class represents the HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """The function defines an an empty line."""
        pass

    def default(self, arg):
        """In case of errors or invalid input in the cmd module"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        s_sh = re.search(r"\.", arg)
        if s_sh is not None:
            nl = [arg[:s_sh.span()[0]], arg[s_sh.span()[1]:]]
            s_sh = re.search(r"\((.*?)\)", nl[1])
            if s_sh is not None:
                cmm = [nl[1][:s_sh.span()[0]], s_sh.group()[1:-1]]
                if cmm[0] in argdict.keys():
                    cl = "{} {}".format(nl[0], cmm[1])
                    return argdict[cmm[0]](cl)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """The fct of the command to quit the program."""
        return True

    def do_EOF(self, arg):
        """The fct for EOF signal to quit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        The function to create a new class instance and print the identifier.
        """
        nl = parse(arg)
        if len(nl) == 0:
            print("** class name missing **")
        elif nl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(nl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Prints the string representation of a class instance of a id.
        """
        nl = parse(arg)
        obdt = storage.all()
        if len(nl) == 0:
            print("** class name missing **")
        elif nl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(nl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(nl[0], nl[1]) not in obdt:
            print("** no instance found **")
        else:
            print(obdt["{}.{}".format(nl[0], nl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Destroy a class instance in a particular  id."""
        nl = parse(arg)
        obdt = storage.all()
        if len(nl) == 0:
            print("** class name missing **")
        elif nl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(nl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(nl[0], nl[1]) not in obdt.keys():
            print("** no instance found **")
        else:
            del obdt["{}.{}".format(nl[0], nl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Prints string representations of all instances of a class.
        If the class is not defined, prints the instantiated objects."""
        nl = parse(arg)
        if len(nl) > 0 and nl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(nl) > 0 and nl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(nl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        nl = parse(arg)
        i = 0
        for obj in storage.all().values():
            if nl[0] == obj.__class__.__name__:
                i += 1
        print(i)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update or add a pair or key & value in a class instance defined
        by id"""
        nl = parse(arg)
        obdt = storage.all()

        if len(nl) == 0:
            print("** class name missing **")
            return False
        if nl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(nl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(nl[0], nl[1]) not in obdt.keys():
            print("** no instance found **")
            return False
        if len(nl) == 2:
            print("** attribute name missing **")
            return False
        if len(nl) == 3:
            try:
                type(eval(nl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(nl) == 4:
            obj = obdt["{}.{}".format(nl[0], nl[1])]
            if nl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[nl[2]])
                obj.__dict__[nl[2]] = valtype(nl[3])
            else:
                obj.__dict__[nl[2]] = nl[3]
        elif type(eval(nl[2])) == dict:
            obj = obdt["{}.{}".format(nl[0], nl[1])]
            for k, v in eval(nl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

