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


def bubbleSort(ll):
    lll = ll.copy()
    length = len(lll)
    for i in range(length):
        for j in range(i + 1, length):
            if lll[i] >= lll[j]:
                lll[i], lll[j] = lll[j], lll[i]
    return lll


def merge(l1, l2):
    toRet = []
    while not (len(l1) == 0) and not (len(l2) == 0):
        if l1[0] < l2[0]:
            toRet.append(l1[0])
            l1 = l1[1:]
        else:
            toRet.append(l2[0])
            l2 = l2[1:]
    for n in l1:
        toRet.append(n)
    for n in l2:
        toRet.append(n)
    return toRet


def mergeSort(ll):
    if len(ll) < 2:
        return ll
    else:
        length = len(ll)
        a, b = ll[:length//2], ll[(length//2):]
        c = merge(mergeSort(a), mergeSort(b))
        return c

def quickSort(ll):
    def partition(l):
        greater = [i for i in l[1:] if i > l[0]]
        less = [i for i in l[1:] if i <= l[0]]
        pivot = l[0]
        return less, pivot, greater
    if len(ll) < 2:
        return ll
    else:
        a, b, c = partition(ll)
        toRet = quickSort(a)
        toRet.append(b)
        toRet.extend(quickSort(c))
        return toRet


ll = [random.randint(0, 100) for i in range(15)]
print("unsorted", ll)
print("selection sort", selectionSort(ll))
print("insertion sort", insertionSort(ll))
print("Bubble sort", bubbleSort(ll))
print("Merge sort", mergeSort(ll))
print("Quick sort", quickSort(ll))