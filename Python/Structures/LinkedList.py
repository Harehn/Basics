class slNode:
    def __init__(self, x, nextNode=None):
        self.value = x
        self.nextNode = nextNode

    def __str__(self):
        return str(self.value) + ", " + str(self.nextNode) if self.nextNode else str(self.value)

    def insert(self, n):
        if self.nextNode is not None:
            self.nextNode.insert(n)
        else:
            self.nextNode = slNode(n)
        return self


# comp takes two values x (value to be inserted) and y (current value)
# returns True if x is to be inserted rn
def insertInOrder(root, n, comp=(lambda x, y: (x < y))):
    # if self.head is None:
    #     self.head = slNode(n)
    if root is None:
        return slNode(n)
    if root.nextNode is None:
        root.nextNode = slNode(n)
        return root
    elif comp(n, root.value):
        return slNode(root.value, insertInOrder(root.nextNode, n, comp))
    else:
        return slNode(n, root)


class sList:
    def __init__(self, n: slNode = None):
        self.head = n

    def insert(self, n):
        if self.head is None:
            self.head = slNode(n)
        else:
            self.head.insert(n)

    def insertInOrder(self, n):
        self.head = insertInOrder(self.head, n)

    def __str__(self):
        return str(self.head)


# ll = sList(slNode(1, slNode(2)))
ll = sList()
for i in range(20):
    import random
    ll.insertInOrder(random.randint(0, 100))
print(ll)
# ll.ss()
# print(ll.head.value)
