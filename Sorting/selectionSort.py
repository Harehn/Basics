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
    def insertElement(l, e):
        lll = l.copy()
        for index, element in enumerate(l):
            if element >= e:
                lll.insert(index, e)
                break
        else:
            lll.insert(len(l), e)
        return lll
    toRet = []
    for el in l:
        #print(el, toRet)
        toRet = insertElement(toRet, el)
    return toRet

def bubbleSort(lll):
    ll = lll.copy()
    length = len(lll)
    for i in range(length):
        for j in range(i + 1, length):
            if lll[i] >= lll[j]:
                lll[i], lll[j] = lll[j], lll[i]
    return lll


ll = [random.randint(0, 100) for i in range(15)]
print("unsorted", ll)
print("selection sort", selectionSort(ll))
print("insertion sort", insertionSort(ll))
print("Bubble sort", bubbleSort(ll))
