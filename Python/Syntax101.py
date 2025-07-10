# Comment with #


# Values, variable and assignments
# Variables are case sensitive
# Assignment is not equality
string = "String"
integer = 123
float_number = 123.123

# Examples of strings
"Hello"
'World'
"123"
""  # Empty String

# Some words are reserved for keywords. Type the following in the terminal to get all keywords
# help("keywords")

# snake_case
# Uses underscore
my_favourite_position = "sitting"

# Variable names should be short, but not too short. And descriptive

# type() gives you the type of the value
type(3)
type(str)

# type casting/conversion
int(3.1)
float("2.3")
str(33)

int("10", 2)  # second argument is the base.
# Output is 2 in this case.
# Default base is 10


# The following is going to give a type error
try:
    print("COMP" + 202)
except TypeError as te:
    print(te)

# Correct way
print("COMP" + str(202))

# incrementing as example of reassignment of value
x = 0
x = x + 1  # x is now equal to 2

# variables are object references, even for primitive types
# object disappear after all references to them are destroyed
a = 1
a = "cat"

# Illegal assignments
try:
    # 7 = x Won't even compile
    # 3 = y + 2
    pass
except:
    pass

####################
var = "global"


def f():
    global var  # makes it so that the next calls refer to the global scope
    var = "changed"


del var  # removes all prior references to var
