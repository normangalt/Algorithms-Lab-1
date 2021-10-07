"Merge sort algortihms"

import time

def merge_sort(unsorted_array):
    """
    Sorts a given array using merge sort algorithm.

    Args:
        unsorted_array (list, optional): input array. Defaults to [].
    """    
    start = time.time()
    comparisons = merge_call(unsorted_array, 0, len(unsorted_array))
    return time.time() - start, comparisons

def merge_call(unsorted_array: list = [], lindex: int = 0, rindex: int = 0, comparisons = 0):
    """
    Sorts a given array using merge sort algorithm.

    Args:
        unsorted_array (list, optional): input array. Defaults to [].
        lindex (int, optional): beginning index for the array. Defaults to 0.
        rindex (int, optional): last index for the array. Defaults to 0.

    Returns:
        list: sorted array.
    """ 
    if 1 < rindex - lindex:
        qindex = (rindex + lindex)//2
        comparisons = merge_call(unsorted_array, lindex, qindex) + \
                      merge_call(unsorted_array, qindex, rindex) + \
                      merge(unsorted_array, lindex, qindex,  rindex)

    return comparisons

def merge(array, lindex, qindex, rindex):
    """
    Merges two arrays in mergesort algorithm.

    Args:
        array ([list]): input array.
        lindex ([int]): beginning index for the array.
        qindex ([int]): end index for the array.
        rindex ([int]): last index for the array.

    Returns:
        list: two arrays merged.
    """
    comparisons = 3
    left_part = []
    right_part = []

    partition1 = qindex - lindex
    partition2 = rindex - qindex

    for index in range(partition1):
        left_part.append(array[lindex + index])

    for index in range(partition2):
        right_part.append(array[qindex + index])

    left_part.append(None)
    right_part.append(None)

    index = 0
    jindex = 0
    for kindex in range(lindex, rindex):
        if left_part[index] is None or right_part[jindex] is None:
            break
    
        comparisons += 1
        if left_part[index] <= right_part[jindex]:
            array[kindex] = left_part[index]
            index += 1
        
        else:
            array[kindex] = right_part[jindex]
            jindex += 1
    
    while left_part[index] is not None and kindex < rindex:
        array[kindex] = left_part[index]
        kindex += 1
        index +=1

    while right_part[jindex] is not None and kindex < rindex:
        comparisons += 1
        array[kindex] = right_part[jindex]
        kindex += 1
        jindex +=1

    return comparisons
