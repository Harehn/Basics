class quickerList:
    def __init__(self, ll=[]):
        self.ll = ll
        self.length = len(ll)

    def get(self, i):
        return self.ll[i]

    def set(self, i, e):
        self.ll[i] = e

    def add(self, i, e):
        self.ll.insert(i, e)
        self.length += 1

    def removei(self, i):
        self.ll.pop(i)
        self.length -= 1

    def removee(self, e):
        self.ll.remove(e)
        self.length -= 1

    def clear(self):
        self.ll.clear()
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

