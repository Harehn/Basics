class Queue:
    def __init__(self, arr=[]):
        self.arr = arr

    def isEmpty(self):
        return self.arr == []

    def enqueue(self, el):
        self.arr.append(el)

    def dequeue(self):
        return self.arr.pop(0)

    def __str__(self):
        return str(self.arr)


m9 = Queue(list(range(9)))
print(m9)
print(m9.dequeue())
print(m9)
print(m9.enqueue(9))
print(m9)