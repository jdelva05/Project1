import time
import random
from memory_profiler import memory_usage


# Function to perform the insertion sort
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val
    return arr


# Partition function for quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j


# Hybrid function -> Quick + Insertion sort
def hybrid_quick_sort(arr, low, high):
    while low < high:

        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            pivot = partition(arr, low, high)

            # Optimised quicksort which works on
            # the smaller arrays first
            if pivot - low < high - pivot:
                hybrid_quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot - 1

    return arr


def test_sorting_algorithm(sort_func):
    assert sort_func([], 0, -1) == []
    assert sort_func([5], 0, 0) == [5]
    assert sort_func([5, 5, 5, 5], 0, 3) == [5, 5, 5, 5]
    assert sort_func([1, 2, 3, 4, 5], 0, 4) == [1, 2, 3, 4, 5]
    assert sort_func([5, 4, 3, 2, 1], 0, 4) == [1, 2, 3, 4, 5]

    for _ in range(10):  # Testing random arrays
        arr = [random.randint(1, 1000) for _ in range(100)]
        assert sort_func(arr.copy(), 0, 99) == sorted(arr)

    print("All tests passed!")


def benchmark(sort_func, size):
    arr = [random.randint(1, 1000) for _ in range(size)]

    start_time = time.time()
    sort_func(arr, 0, size - 1)
    return time.time() - start_time


def memory_benchmark(sort_func, size):
    arr = [random.randint(1, 1000) for _ in range(size)]
    mem_usage = memory_usage((sort_func, (arr, 0, size - 1)), interval=0.1, timeout=1)
    return max(mem_usage) - mem_usage[0]


if __name__ == "__main__":
    # Testing
    test_sorting_algorithm(hybrid_quick_sort)

    # Benchmarking
    sizes = [100, 500, 1000, 5000, 10000, 50000]

    times_hybrid = [benchmark(hybrid_quick_sort, s) for s in sizes]
    print("Hybrid QuickSort times:", times_hybrid)

    times_python_sorted = [benchmark(lambda arr, _, __: arr.sort(), s) for s in
                           sizes]  # Using list.sort() instead of sorted()
    print("Python list.sort() times:", times_python_sorted)

    mem_hybrid = [memory_benchmark(hybrid_quick_sort, s) for s in sizes]
    print("Hybrid QuickSort Memory Usage:", mem_hybrid)

