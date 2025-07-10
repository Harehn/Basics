import time as t
def makearr1(num):
    t1 = t.time()
    arr = []
    for i in range(num):
        arr.append(i)
    t2 = t.time()
    print("{}) {} took {} seconds".format(num, ))