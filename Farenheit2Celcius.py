
# Use of the following formula
# (F-32)*5/9 = C

print("The following program converts fahrenheit to celsius. Enter 0 to exit")
while True:
    f = int(input("Enter the temperature in Fahrenheit: "))
    if f == 0 :
        if input("Are you sure you want to exit?(y/n)") == 'y':
            exit(0)
    print(f, "Fahrenheit is", ((f-32)*5/9), "in celsius")