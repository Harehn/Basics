from _collections import defaultdict
import random

def c_hash(num):
    random.seed(num)
    return random.randint(0, 100)


class hashMap:
    def __init__(self, ll=[]):
        self.d = defaultdict(list)
        for el in ll:
            self.insert(el)

    def insert(self, n):
        self.d[c_hash(n)].append(n)

    def is_present(self, el):
        return el in self.d[c_hash(el)]

    def remove(self,el):
        if el in self.d[c_hash(el)]:
            self.d[c_hash(el)].remove(el)
            return True
        return False

    def __str__(self):
        return "".join(["{} : {}\n".format(k, v) for k, v in self.d.items()])


h = hashMap(list(range(100)))
print(h)
print(h.is_present(54))
print(h.remove(54))
print(h.is_present(54))