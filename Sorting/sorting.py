import random


def my_timer(orig_fun):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        output = orig_fun(*args, **kwargs)
        t2 = time.time()
        # print("{} ran in {} seconds".format(orig_fun.__name__, (t2 - t1)))
        return output, t2-t1

    return wrapper


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


def treeSort(lll):
    from Structures.Trees import tree
    t = tree()
    for el in lll:
        t.insert(el)
    return t.traverse()

def countsort(lll):
    counts = [0 for i in range(101)]
    for num in lll:
        counts[num] += 1
    prevcount = 0
    for i in range(len(counts)):
        counts[i] += prevcount
        prevcount = counts[i]
    sortedarr = [0 for i in lll]
    print(counts)
    for num in lll:
        sortedarr[counts[num]-1] = num
        counts[num] -= 1
    return sortedarr

def gnomesort(lll):
    sortedarr = [i for i in lll]
    i = 0
    reachedEnd = False
    length = len(sortedarr)
    while not reachedEnd:
        if i == 0:
            i += 1
        if sortedarr[i] >= sortedarr[i - 1]:
            i += 1
        else:
            sortedarr[i], sortedarr[i - 1] = sortedarr[i - 1], sortedarr[i]
            i -= 1
        if i == length:
            reachedEnd = True
    return sortedarr



class Sort:
    algorithms = [selectionSort, insertionSort, bubbleSort, mergeSort, quickSort, treeSort, countsort, gnomesort]
    def __init__(self):
        self.sortDicts = {(i+1): (fun.__name__, my_timer(fun)) for i, fun in enumerate(self.algorithms)}

    def sort_all(self, num):
        ll = [random.randint(0, 100) for i in range(num)]
        results = {}
        for k, (name, fun) in self.sortDicts.items():
            r = fun(ll) if len(ll) < 50 else (None, fun(ll)[1])
            results[k] = {
                "name": name,
                "time": r[1],
                "results": list(r[0]) if r[0] else r[0]
            }
        return results


def toStr(results):
    return "\n".join([str(k1) + ")" + "\n".join(["\t{} : {}".format(k2, vals2)
                                                 for k2, vals2 in val1.items()]) for (k1, val1) in results.items()])


print(toStr(Sort().sort_all(25)))