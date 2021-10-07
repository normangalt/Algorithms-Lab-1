"Shellsort algortihms"

import time

def shellsort(unsorted_array: list = []):
    """
    Sorts a given array using shellsort algorithm.

    Args:
        unsorted_array (list, optional): input array. Defaults to [].

    Returns:
        list: sorted array.
    """
    start = time.time()
    comparisons = 2
    length = len(unsorted_array)
    hstep = 1
    while hstep < length/3:
        comparisons += 1
        hstep = hstep*3 + 1

    while hstep >= 1:
        comparisons += 1
        for index in range(hstep, length):
            jindex = index
            comparisons += 1
            while unsorted_array[jindex - hstep] > unsorted_array[jindex] and jindex >= hstep:
                comparisons += 1
                temporary = unsorted_array[jindex]
                unsorted_array[jindex] = unsorted_array[jindex - hstep]
                unsorted_array[jindex - hstep] = temporary
                jindex -= hstep

        hstep //= 3

    return time.time() - start, comparisons
