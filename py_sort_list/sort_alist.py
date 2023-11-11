
from contextlib import contextmanager
import tracemalloc
import datetime



def bubble_sort(array):
    swap_counter = 0
    compare_operations_counter = 0  # O(n^2) -> nested loop
    # loop to access each array element
    for i in range(len(array)):
        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            compare_operations_counter+=1
            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:
                swap_counter+=1
                # swapping elements if elements
                # are not in the intended order
                swap_members(j, j+1, array)
    if TRACE:
        print(f'n = length of list: {len(array)}')
        print(f'compare operations: {compare_operations_counter}')
        print(f'swap    operations: {swap_counter}')
    return array


def merge_sort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1
    return array


def swap_members(i,j, alist) -> list:
    temp_member = alist[i]
    alist[i] = alist[j]
    alist[j] = temp_member
    return alist


def sort_a_list(alist = []) -> list:
    """
    Naive bubble sort, easy to remember
    """
    swap_counter = 0
    compare_operations_counter = 0  # O(n^2) -> nested loop
    for i in range(len(alist)):
        for j in range(len(alist)):
            compare_operations_counter+=1
            if alist[i] < alist[j]:
                swap_counter +=1
                swap_members(i,j,alist)
    if TRACE:
        print(f'n = length of list: {len(alist)}')
        print(f'compare operations: {compare_operations_counter}')
        print(f'swap    operations: {swap_counter}')
    return alist

def get_sort_method(method_name = ''):
    DEFAULT_METHOD = 'sort_a_list'
    if not method_name in globals():
        # raise KeyError(f'cant find sort method: {method_name}')
        print(f'setting default method as: {DEFAULT_METHOD}')
        method_name = DEFAULT_METHOD
    sort_method = globals()[method_name]
    return sort_method


def test_execution(alist = [], expexted_result = [], method_name = ''):
    tested_sort_method = get_sort_method(method_name)
    original_list = alist.copy()
    with trace_method_context():
        sorted_list = tested_sort_method(alist)
    print(f'original list is: {original_list}')
    print(f'sorted list ----> {sorted_list}')
    print(f'expected result-> {expexted_result}')


@contextmanager
def trace_method_context():
    start_time = datetime.datetime.now()
    print(f'[{start_time.isoformat()}] -> starting trace of memory usage ->')
    tracemalloc.start()
    yield
    print_memory_usage()
    tracemalloc.stop()
    finish_time = datetime.datetime.now()
    print(f'[{finish_time.isoformat()}] -> finished tracing memory usage -<')


def print_memory_usage():
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    if top_stats:
        print(f'[ Top 10 ] out of: {len(top_stats)}')
        for stat in top_stats[:10]:
            print(stat)
    first_size, first_peak = tracemalloc.get_traced_memory()
    print(f'*** current size: {first_size}, max peak: {first_peak} ***')


if __name__ == "__main__":
    TRACE=True  # flag for trace and debugging
    alist = [1,2,3,5,4]
    test_execution(alist, [1,2,3,4,5])
    print('*'*60)
    alist = [1,5,3,1,-1] + [1,5,3,1,-2,100,0,0,20]
    expected_result = [-2, -1, 0, 0, 1, 1, 1, 1, 3, 3, 5, 5, 20, 100]
    test_execution(alist, expected_result)
    print('*'*60)
    alist = [1,5,3,1,-1] + [1,5,3,1,-2,100,0,0,20]
    expected_result = [-2, -1, 0, 0, 1, 1, 1, 1, 3, 3, 5, 5, 20, 100]
    test_execution(alist, expected_result, 'bubble_sort')
    print('*'*60)
    alist = [1,5,3,1,-1] + [1,5,3,1,-2,100,0,0,20]
    expected_result = [-2, -1, 0, 0, 1, 1, 1, 1, 3, 3, 5, 5, 20, 100]
    test_execution(alist, expected_result, 'merge_sort')

