def convert(num, base=2):
    convstr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num != 0:
        convert(num // base, base)
        print(convstr[num % base] ,end="")


def print_convert(num, base=2):
    print(str(num) + " in " + str(base) + " is ", end="")
    convert(num, base)
    print()


while True:
    number = int(input("Enter your desired number (0 to exit) : "))
    if number <= 0:
        print("Exiting program")
        exit(0)
    base = int(input("Enter your desired base: "))
    print_convert(number, base)
