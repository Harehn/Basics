# Comment with #

# 1..0 VARIABLES
# Variables are case sensitive
# snake_case, Uses underscore

string = "String"
integer = 123
float_number = 123.123
my_favourite_position = "sitting"

# 1..1 TYPE, TYPE CASTING
# Some words are reserved for keywords. Type the following in the terminal to get all keywords
# help("keywords")

type(3)  # type() gives you the type of the value

# type casting/conversion
int(3.1)
float("2.3")
str(33)

int("10", 2)  # second argument is the base.
# Output is 2 in this case.
# Default base is 10

# 1..2 OPERATIONS
integer += 3

# 1..3 REMOVING REFERENCES
del integer  # removes all prior references to var

# 1..4 TUPLES
a = 1, 2, "three", (4, 5.0)  # a tuple of 4 values, last value is a tuple of 2 values
tup1 = (50,)  # This is the appropriate syntax for 1 value in the tuple
# a[0] = 3  # this is an illegal assignment because tuples are IMMUTABLE

b, c = 13, 22  # multiple initialisation using tuples

b, c = c, b  # switching values

# 1..4.1 OPERATIONS ON TUPLES
a = a + tup1  # CONCATENATION
max((1, 2, 3)), min(1, 2, 3)
a[-1]  # last character
a[1:3]  # returns tuple from 1 to 3

# 2..0 PRINTING
print("COMP" + str(202))  # cannot concatenate string with int
print("You can write over multiple lines \
using a backlash \
like this")
print("My favourite number is", 5, "!")

# 3..0 Try Catch
try:
    pass
except TypeError as te:
    print(te)

# 4..0 FUNCTIONS
var = "global"
def f(arg1, arg2 = "Fixed"):  # can have arguments with fixed values
    global var  # makes it so that the next calls refer to the global scope
    var = "changed"
    return arg1
