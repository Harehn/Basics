def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selection_sort(arr):
    new_arr = []
    while arr:
        min_arr = min(arr)
        new_arr.append(min_arr)
        arr.remove(min_arr)
    return new_arr


def insertion_sort(arr):
    new_arr = []
    for el in arr:
        index = 0
        for i in range(len(new_arr)):
            if el > new_arr[i]:
                index += 1
        new_arr.insert(index, el)
    return new_arr


def merge_sort(arr):
    def merge(arr1, arr2, result=[]):
        if not arr1:
            result.extend(arr2)
            return result
        if not arr2:
            result.extend(arr1)
            return result
        if arr1[0] > arr2[0]:
            result.append(arr2[0])
            return merge(arr1, arr2[1:], result)
        else:
            result.append(arr1[0])
            return merge(arr1[1:], arr2, result)

    def split(arr1):
        length = len(arr1)
        return [arr1[:length // 2], arr1[length // 2:]]

    # return merge(*split(arr))
    if len(arr) == 1:
        return arr
    arr1, arr2 = split(arr)
    return merge(merge_sort(arr1), merge_sort(arr2))


def quick_sort(arr):
    if len(arr) < 2:
        return arr

    def partition(arr1):
        pivot = arr1[0]
        return [x for x in arr1 if x < pivot], pivot, [x for x in arr1 if x > pivot]

    arr1, pivot, arr2 = partition(arr)
    # return arr1, arr2
    return [*quick_sort(arr1), pivot, *quick_sort(arr2)]


def tree_sort(arr):
    class Node:
        def __init__(self, val_f):
            self.val = val_f
            self.right = None
            self.left = None

        def insert(self, val_f):
            if self.val < val_f:
                if self.right:
                    self.right.insert(val_f)
                else:
                    self.right = Node(val_f)
            else:
                if self.left:
                    self.left.insert(val_f)
                else:
                    self.left = Node(val_f)

        def traverse(self, arr):
            if self.left:
                self.left.traverse(arr)
            arr.append(self.val)
            if self.right:
                self.right.traverse(arr)
            # return arr

    root = Node(arr[0])
    new_arr = []
    for num in arr[1:]:
        root.insert(num)
    root.traverse(new_arr)
    return new_arr


def heap_sort(arr):
    def heapify(arr1, limit, index):
        largest, left, right = index, (2 * index) + 1, (2 * index) + 2
        if left < limit and arr1[left] > arr1[largest]:
            largest = left
        if right < limit and arr1[right] > arr1[largest]:
            largest = right
        if largest != index:
            arr1[index], arr1[largest] = arr1[largest], arr1[index]
            heapify(arr1, limit, largest)

    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)
    # return arr
    for i in range(len(arr)):
        arr[0], arr[-i - 1] = arr[-i - 1], arr[0]
        heapify(arr, len(arr) - i -1, 0)
    return arr


import random
length = 20
RANGE = 10_000
numbers = [random.randint(1, RANGE) for i in range(length)]
print("Numbers:", numbers)
print("Result of bubble sort: ", bubble_sort(numbers.copy()))
print("Result of selection sort: ", selection_sort(numbers.copy()))
print("Result of insertion sort: ", insertion_sort(numbers.copy()))
print("Result of merge sort: ", merge_sort(numbers.copy()))
print("Result of quick sort: ", quick_sort(numbers.copy()))
print("Result of tree sort: ", tree_sort(numbers.copy()))
print("Result of heap sort: ", heap_sort(numbers.copy()))