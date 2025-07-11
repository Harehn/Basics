# help("keywords")
# 1..0 VARIABLES
# 1..1 Comment with #
# 1..2 Variable types
string = "String"
integer = 123
float_number = 123.123
boolean = True

# 1..3 Operations
integer += 3
earth_day = (31 - 9) * 100 / 5 - 20
weeks = 31 / 7  # Float division
weeks = 31 // 7  # Integer division
square = 5 ** 2
string = "This is a " + string

# 1..4 type casting
# type casting/conversion
int(3.1)
float("2.3")
str(33)
bool(0)

int("10", 2)  # second argument is the base.
# Output is 2 in this case.
# Default base is 10

# 1..5 lists
thislist = ["apple", "banana", "cherry"]  # Zero indexed
coordinates = [[0,1], [1,2], [2,3]]
second_x_coordinates = coordinates[1][0]

# 1..6 Other structures
# tuples
a = 1, 2, "three", (4, 5.0)  # a tuple of 4 values, last value is a tuple of 2 values
tup1 = (50,)  # This is the appropriate syntax for 1 value in the tuple
# a[0] = 3  # this is an illegal assignment because tuples are IMMUTABLE
b, c = 13, 22  # multiple initialisation using tuples
b, c = c, b  # switching values
a = a + tup1  # CONCATENATION
max((1, 2, 3)), min(1, 2, 3)
a[-1]  # last character
a[1:3]  # returns tuple from 1 to 3

# dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key, value in thisdict.items():  # thisdict.keys(), thisdict.values()
    pass
mydict = thisdict.copy()

# 1..7 get Variable type
type(3)  # type() gives you the type of the value

# 2..0 INPUT/OUTPUT
# 2..1 printing
print("Python" + str(101))  # cannot concatenate string with int
print("You can write over multiple lines \
using a backlash \
like this")
print("My", "favourite number", "is", 4, "!")  # default separator is " "
print("My", "favourite number", "is", 4, "!", sep=",")
print("Hello", end="")  # So that there is no end line character after the print
print()

# 2..2 User Input
try:
    x = input("Please enter a number:")
    someVar = int(x)
except (TypeError, ValueError) as e:
    print(e)

# 2..3 Console arguments
import sys
print ('argument list', sys.argv)
# first_argument = sys.argv[1]

# 2..4 File IO
try:
    filename = "example.txt"
    out_file = open(filename, 'w+')
    out_file.write("Mercy is a skill this world could use more of.\n")
    out_file.close()
    in_file = open(filename, 'r+')
    lines = in_file.readlines()
    in_file.close()
except:
    pass
# Reading files with context manager
with open("example.txt", 'r+') as infile:
    print(infile.readlines())

# 3..0 LOGIC FLOW
# 3..1 for loop
total = 0
for i in range(12): # 0,..., 11  ||  12 iterations
    total += i
var = 1
# for each
for x in (1, 2, 3):
    var += 1
var = [x/2 for x in (1, 2, 3)]

# 3..2 While loop
while False:
    pass

# 3..3 if else
if 1 in (1, 2, 3):
    var = 1

# 3..4 Switch Case
# The following was introduced in python 3.10
argument = 1
match argument:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2:
        print("two")
    case default:
        print("something")

# 3..5 Ternary operator
var += 3 if 3 in (1, 2, 3) else 0
var = (2, 3) if 3 in (1, 2, 3) else 0  # Workaround
var = [x/2 for x in (1, 2, 3) if (x+1) in (1, 2, 3)] # Combinations

# 3..6 Try Catch
try:
    pass
except TypeError as te:
    print(te)

# 4..0 FUNCTIONS
def add(x,y):
    return x + y
var = "global"
def f(arg1, arg2="Fixed"):  # can have arguments with fixed values
    global var  # makes it so that the next calls refer to the global scope
    var = "changed"
    return arg1
def add2(x, func):
    def new_add(y):
        return func(x,y)
    return new_add
new_func = add2(3, add)
print("Higher order function test:", new_func(4))

# 4..3 lambdas
f2 = lambda arg1: arg1 + 10  # arg1+10 is the output
f3 = lambda arg1: arg1 * 2
f4 = lambda arg1: f3(f3(arg1))
f5 = lambda ff, arg2: ff(arg2)  # functions as variables

# 4.5 overloading
# Python does not have overloading by default
# Use type testing and default arguments to get the desired behaviour


# 7..0 RANDOMNESS
import random
random.seed(a=None)  # seeding
random.randint(0, 1)  # Return a random integer N such that a <= N <= b.
random.choice((1, 2, 3))  # Return a random element from the non-empty sequence seq.


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
