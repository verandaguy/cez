# cez (see-easy)

A Python library for templating/auto-generating C code.

## Sample Program

```python
from cez import types

usint = types.PrimitiveType("unsigned int")
charPtr = types.PrimitiveType("char *")

name = charPtr.declair("name")
age = usint.declair("age")

person = types.Struct("_person", [name, age])
personType = types.TypeDef("Person_s", person)

me = types.Variable("me", personType, "{\"Alex\", 23}")

print(personType.prototype(indent=4))
print(me.prototype(indent=4))
```

Output:
```C
typedef struct _person {
    char * name;
    unsigned int age;
} Person_s;
Person_s me = {"Alex", 23};
```
