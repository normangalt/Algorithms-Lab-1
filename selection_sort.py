"Selection sort algortihms"

import time

def selection_sort(unsorted_array: list = []):
    """
    Sorts a given array using selection sort algorithm.

    Args:
        unsorted_array (list, optional): input array. Defaults to [].

    Returns:
        list: sorted array.
    """
    start = time.time()
    comparisons = 0

    length = len(unsorted_array)
    for index in range(length):
        minimum_index = index
        for jindex in range(index + 1, length):
            comparisons += 1
            if unsorted_array[jindex] < unsorted_array[minimum_index]:
                minimum_index = jindex
        
        temporary = unsorted_array[index]
        unsorted_array[index] = unsorted_array[minimum_index]
        unsorted_array[minimum_index] = temporary
    
    return time.time() - start, comparisons
