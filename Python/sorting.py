def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

import random
length = 20
RANGE = 10_000
numbers = [random.randint(1, RANGE) for i in range(length)]
print(bubble_sort(numbers.copy()))
