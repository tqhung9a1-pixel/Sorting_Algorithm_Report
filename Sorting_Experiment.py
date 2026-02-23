import numpy as np
import pandas as pd
import time

from quicksort import quicksort
from mergesort import merge_sort
from heapsort import heap_sort

# HÀM TIME READER
def time_reader(sort_func, arr):
    arr_copy = arr.copy()
    start = time.perf_counter()
    result = sort_func(arr_copy)
    stop = time.perf_counter()
    return (stop - start) * 1000


# ĐỌC DỮ LIỆU
df = pd.read_csv("data.csv")

dataset = [df[col].tolist() for col in df.columns]

# TEST
for i, data in enumerate(dataset):
    print(f"\n===== Arr {i + 1} =====")

    print(f"Quick Sort: {time_reader(quicksort, data):.2f} ms")

    print(f"Merge Sort: {time_reader(merge_sort, data):.2f} ms")

    print(f"Heap Sort: {time_reader(heap_sort, data):.2f} ms")

    print(f"Python sort: {time_reader(lambda x: sorted(x), data):.2f} ms")

    np_data = np.array(data)
    start = time.perf_counter()
    np.sort(np_data)
    stop = time.perf_counter()
    print(f"NumPy sort: {(stop - start) * 1000:.2f} ms")
