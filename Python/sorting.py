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

import random
length = 20
RANGE = 10_000
numbers = [random.randint(1, RANGE) for i in range(length)]
print(bubble_sort(numbers.copy()))
print(selection_sort(numbers.copy()))
