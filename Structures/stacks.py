class Stack:
    def __init__(self, arr=[]):
        self.arr = arr

    def isEmpty(self):
        return self.arr == []

    def push(self, el):
        self.arr.append(el)

    def pop(self):
        return self.arr.pop(len(self.arr) -1 )

    def __str__(self):
        return str(self.arr)


# m9 = Stack(list(range(9)))
# print("The mighty nein is :", m9)
# print("The return of m9.pop() is :", m9.pop())
# print("The mighty nein is now :", m9)
# print("The return of m9.push(9) is :",m9.push(9))
# print("The mighty nein is now :",m9)