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

# 1..5 LISTS
thislist = ["apple", "banana", "cherry"]


# 1..6 DICTIONARIES
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key, value in thisdict.items():  # thisdict.keys(), thisdict.values()
    pass
mydict = thisdict.copy()

# 2..0 PRINTING
print("COMP" + str(202))  # cannot concatenate string with int
print("You can write over multiple lines \
using a backlash \
like this")
print("My favourite number is", 5, "!", sep=",")  # default separator is ","
print("llllll", end="")  # So that there is no end line character after the print


# 3..0 Try Catch
try:
    pass
except TypeError as te:
    print(te)

# 4..0 FUNCTIONS
var = "global"


def f(arg1, arg2="Fixed"):  # can have arguments with fixed values
    global var  # makes it so that the next calls refer to the global scope
    var = "changed"
    return arg1


# 4..1 LAMBDAS
f2 = lambda arg1: arg1 + 10  # arg1+10 is the output
f3 = lambda arg1: arg1 * 2
f4 = lambda arg1: f3(f3(arg1))
f5 = lambda ff, arg2: ff(arg2)  # functions as variables

# 5..0 LOGIC
# 5..1 IF ELSE
if 1 in (1, 2, 3):
    var = 1
var += 3 if 3 in (1, 2, 3) else 0
var = (2, 3) if 3 in (1, 2, 3) else 0  # Workaround

# 5..2 FOR LOOP
var = 1
for x in (1, 2, 3):
    var += 1
var = [x/2 for x in (1, 2, 3)]

# 5..3 While LOOP
while False:
    pass

# 5..4 COMBINATION
var = [x/2 for x in (1, 2, 3) if (x+1) in (1, 2, 3)]

# 6..0 INPUT
x = input("Please enter something")
try:
    someVar = int(input())
except (TypeError, ValueError) as e:
    print(e)

# 7..0 RANDOMNESS
import random
random.seed(a=None)  # seeding
random.randint(0, 1)  # Return a random integer N such that a <= N <= b.
random.choice((1, 2, 3))  # Return a random element from the non-empty sequence seq.

# 8..0 FILE IO
try:
    in_file = open("Filename", 'r+')
    lines = in_file.readlines()
    in_file.close()
    out_file = open("Filename", 'w+')
    out_file.write("Refer to .... for formatting rules\n")
    out_file.close()
except:
    pass


class Obj:
    def __init__(self, x, y=2):
        self.x = x
        self.y = y


class Obj2(Obj):
    def __init__(self, x, y=2):
        super(x, y)

    def __str__(self):
        return ""

    def __hash__(self):
        return 1
