class tree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val is None:
            self.val = val
        elif self.val > val:
            if self.left is None:
                self.left = tree(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = tree(val)
            else:
                self.right.insert(val)

    def traverse(self):
        if self.left is not None:
            yield from self.left.traverse()
        yield self.val
        if self.right is not None:
            yield from self.right.traverse()

# t = tree()
# for i in range(17):
#     import random
#     t.insert(random.randint(0, 100))
# for i in t.traverse():
#     print(i, end=" ")