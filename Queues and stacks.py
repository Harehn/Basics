class slNode:
    def __init__(self, x, nextNode =None):
        self.value = x
        self.nextNode = nextNode

class sList:
    def __init__(self, n: slNode = None):
        self.head = n

    def insert(self, n):
        if not self.head:
            self.head = n
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = n


    def ss(self):
        curr = self.head
        print(curr.value)
        while curr.next:
            print(curr.value)
            curr = curr.next

ll = sList(slNode(1, slNode(2)))
ll.ss()
# print(ll.head.value)