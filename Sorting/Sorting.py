import random


def my_timer(orig_fun):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        output = orig_fun(*args, **kwargs)
        t2 = time.time()
        print("{} ran in {} seconds".format(orig_fun.__name__, (t2 - t1)))
        return output

    return wrapper


@my_timer
def selectionSort(ll):
    l = ll.copy()
    toRet = []
    for i in range(len(l)):
        el = max(l)
        toRet.append(el)
        l.remove(el)
    return list(reversed(toRet))


@my_timer
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


@my_timer
def bubbleSort(ll):
    lll = ll.copy()
    length = len(lll)
    for i in range(length):
        for j in range(i + 1, length):
            if lll[i] >= lll[j]:
                lll[i], lll[j] = lll[j], lll[i]
    return lll


@my_timer
def mergeSort(lll):
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

    def helper(ll):
        if len(ll) < 2:
            return ll
        else:
            length = len(ll)
            a, b = ll[:length//2], ll[(length//2):]
            c = merge(helper(a), helper(b))
            return c
    return helper(lll)

@my_timer
def quickSort(lll):
    def helper(ll):
        def partition(l):
            greater = [i for i in l[1:] if i > l[0]]
            less = [i for i in l[1:] if i <= l[0]]
            pivot = l[0]
            return less, pivot, greater
        if len(ll) < 2:
            return ll
        else:
            a, b, c = partition(ll)
            toRet = helper(a)
            toRet.append(b)
            toRet.extend(helper(c))
            return toRet
    return helper(lll)


ll = [random.randint(0, 100) for i in range(15000)]
# print("0) unsorted", ll)
# print("1) python default sort", sorted(ll))
# print("2) selection sort", selectionSort(ll))
# print("3) insertion sort", insertionSort(ll))
# print("4) Bubble sort", bubbleSort(ll))
# print("5) Merge sort", mergeSort(ll))
# print("6) Quick sort", quickSort(ll))
selectionSort(ll)
insertionSort(ll)
bubbleSort(ll)
mergeSort(ll)
quickSort(ll)