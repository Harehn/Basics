
def swap_values(x, y):
    #x, y := y, x
    temp = x
    x := y
    y := temp


def print_vals(x, y):
    print("The value of a is",x ," and the value of b is",y)


a = 3
b = 7
print_vals(a, b)
swap_values(a, b)
print_vals(a, b)

