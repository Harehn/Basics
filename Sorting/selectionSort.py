import random


def selectionSort(l):
    toRet = []
    for i in range(len(l)):
        el = max(l)
        toRet.append(el)
        l.remove(el)
    return list(reversed(toRet))


ll = [random.randint(0, 100) for i in range(15)]
print(ll)
print(selectionSort(ll))
