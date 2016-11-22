""" CEZ - Types

This module contains the classes for creating C types from primative
types.  Some of the basic

"""

import sys
import re

CTYPE_NAME=r"[a-zA-Z_][a-zA-Z0-9_]*"

class PrimativeType(object):
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def declair(self, varname: str):
        return Variable(varname, self)

    def prototype(self, indent: int=None):
        return str(self.name)

class TypeDef(object):
    def __init__(self, name: str, base):
        self._name = name
        self._base = base

    @property
    def name(self) -> str:
        return self._name

    @property
    def base(self):
        return self._base

    def declair(self, varname: str):
        return Variable(varname, self)

    def prototype(self, indent: int=None):
        return ("typedef {base} {name};"
                .format(name=self.name,
                        base=self.base.prototype(indent=indent)))

class Variable(object):
    def __init__(self, name: str, ctype, default=None):
        self._name = name
        self._ctype = ctype
        self._default = default

    @property
    def name(self) -> str:
        return self._name

    @property
    def ctype(self):
        return self._ctype

    @property
    def default(self):
        return self._default

    def prototype(self, indent: int=None):
        if self.default is not None:
            return "{type} {name} = {default};".format(type=self.ctype.name,
                                                       name=self.name,
                                                       default=self.default)
        else:
            return "{type} {name};".format(type=self.ctype.name,
                                           name=self.name)

class Struct(object):
    def __init__(self, name, attributes: list):
        self._name = name
        self._attributes = list(attributes)

    @property
    def name(self) -> str:
        return "struct {name}".format(name=self._name)

    @property
    def attributes(self):
        return self._attributes[:]

    def prototype(self, indent: int=0):
        return ("{name} {{\n{indent}{attributes}\n}}"
                .format(name=self.name,
                        indent="".join([" "]*indent),
                        attributes=("\n{indent}"
                                    .format(indent="".join([" "]*indent))
                                    .join([attr.prototype(indent=indent)
                                           for attr in self.attributes]))))

class Union(object):
    pass

class Enumeration(object):
    pass

class BitField(object):
    def __init__(self, base, name=None):
        self._


def main(*argv):
    usint = PrimativeType("unsigned int")
    charPtr = PrimativeType("char *")

    name = charPtr.declair("name")
    age = usint.declair("age")

    person = Struct("_person", [name, age])
    personType = TypeDef("Person_s", person)

    me = Variable("me", personType, "{\"Alex\", 23}")

    print(personType.prototype(indent=4))
    print(me.prototype(indent=4))
    return 0

if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
