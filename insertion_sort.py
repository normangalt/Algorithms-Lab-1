"Insertion sort algortihms"

import time 

def insertion_sort(unsorted_array: list = []):
    """
    Sorts a given array using insertion sort algorithm.

    Args:
        unsorted_array (list, optional): input array. Defaults to [].

    Returns:
        list: sorted array.
    """    
    start = time.time()
    comparisons = 0
    length = len(unsorted_array)
    for index in range(1, length):
        jindex = index
        comparisons += 1
        while unsorted_array[jindex - 1] > unsorted_array[jindex] and jindex > 0:
            comparisons += 1
            temporary = unsorted_array[jindex - 1]
            unsorted_array[jindex - 1] = unsorted_array[jindex]
            unsorted_array[jindex] = temporary
            jindex -= 1
        
    return time.time() - start, comparisons
