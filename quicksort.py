# Quicksort implementation full code
import random
import time
import sys
from typing import List, Callable

sys.setrecursionlimit(10000)

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort_recursive(arr: List[int], low: int, high: int):
    if low < high:
        p = partition(arr, low, high)
        quicksort_recursive(arr, low, p-1)
        quicksort_recursive(arr, p+1, high)

def quicksort_sort(arr: List[int]):
    if arr:
        quicksort_recursive(arr, 0, len(arr)-1)

def randomized_partition(arr: List[int], low: int, high: int) -> int:
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return partition(arr, low, high)

def randomized_quicksort_recursive(arr: List[int], low: int, high: int):
    if low < high:
        p = randomized_partition(arr, low, high)
        randomized_quicksort_recursive(arr, low, p-1)
        randomized_quicksort_recursive(arr, p+1, high)

def randomized_quicksort_sort(arr: List[int]):
    if arr:
        randomized_quicksort_recursive(arr, 0, len(arr)-1)

def make_input(n: int, kind: str):
    if kind == "random":
        return [random.randint(0, 1000000) for _ in range(n)]
    if kind == "sorted":
        return list(range(n))
    if kind == "reverse":
        return list(range(n, 0, -1))
    raise ValueError("Unknown type")

def time_sort(func: Callable[[List[int]], None], arr: List[int]) -> float:
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return end - start

def run_experiments():
    print("Demo:")
    demo=[10,7,8,9,1,5]
    det=demo.copy(); quicksort_sort(det)
    rnd=demo.copy(); randomized_quicksort_sort(rnd)
    print(det, rnd)

    sizes=[1000,3000,5000]
    types=["random","sorted","reverse"]
    versions=[("Det", quicksort_sort), ("Rand", randomized_quicksort_sort)]

    for n in sizes:
        for t in types:
            for name, func in versions:
                arr=make_input(n,t)
                tm=time_sort(func, arr)
                print(n,t,name,tm)

if __name__=="__main__":
    run_experiments()
