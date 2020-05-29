import random


def selectionSort(ll):
    l = ll.copy()
    toRet = []
    for i in range(len(l)):
        el = max(l)
        toRet.append(el)
        l.remove(el)
    return list(reversed(toRet))


def insertionSort(l):
    toRet = []
    for el in l:
        #print(el, toRet)
        toRet = insertElement(toRet, el)
    return toRet

def insertElement(l, e):
    lll = l.copy()
    for index, element in enumerate(l):
        if element >= e:
            lll.insert(index, e)
            break
    else:
        lll.insert(len(l), e)
    return lll


ll = [random.randint(0, 100) for i in range(15)]
print("unsorted", ll)
print("selection sort", selectionSort(ll))
print("insertion sort", insertionSort(ll))
