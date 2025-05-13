import time 
import matplotlib.pyplot as plt
import tracemalloc
import random
import time
import tracemalloc
import random

arr1 = [random.randint(0, 1000) for _ in range(999)]


def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def measure_time(sort_func, arr):
    start = time.time()
    sort_func(arr.copy())
    end = time.time()
    return end - start


def measure_memory(sort_func, arr):
    tracemalloc.start()
    sort_func(arr.copy())
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak  


bubble_time = measure_time(bubble, arr1)
merge_time = measure_time(merge_sort, arr1)
quick_time = measure_time(quick_sort, arr1)

print(f"Bubble Sort Time: {bubble_time:.6f} sec")
print(f"Merge Sort Time: {merge_time:.6f} sec")
print(f"Quick Sort Time: {quick_time:.6f} sec")


bubble_memory = measure_memory(bubble, arr1)
merge_memory = measure_memory(merge_sort, arr1)
quick_memory = measure_memory(quick_sort, arr1)

print(f"Bubble Sort Peak Memory: {bubble_memory} bytes")
print(f"Merge Sort Peak Memory: {merge_memory} bytes")
print(f"Quick Sort Peak Memory: {quick_memory} bytes")
x = [bubble_time, merge_time, quick_time]
y = [bubble_memory, merge_memory, quick_memory]

plt.plot(x, y)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Graph')

plt.show()
