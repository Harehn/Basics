
# Comment with #

# printing; Use quotation marks ""
print("Hello World!")  # inline comment
print("My favourite number is", 5, "!")
print("Hello" + " World!")  # String concatenation
print("\n" + "\'" + "\t" ) # Newline character, quotation mark, tab
print("You can write over multiple lines \
       using a backlash \
      like this")


# Examples of strings
"Hello"
'World'
"123"
"" # Empty String

# Values, variable and assignments
str = "String"
integer = 123
float_number = 123.123

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


