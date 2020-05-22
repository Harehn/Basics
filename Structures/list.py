class simpleList:
    def __init__(self, ll=[]):
        self.ll = ll

    def get(self, i):
        return self.ll[i]

    def set(self, i, e):
        self.ll[i] = e

    def add(self, i, e):
        self.ll.insert(i, e)

    def removei(self, i):
        self.ll.pop(i)

    def removee(self, e):
        self.ll.remove(e)

    def clear(self):
        self.ll.clear()

    def isEmpty(self):
        return len(self.ll) == 0

    def size(self):
        return len(self.ll)

