"Generators of the experiments for sorting algorithms tests"

import random
from math import ceil

def generate_array(number: int):
    """
    Generates an array of size n consisting of random elements .

    Args:
        number (int): size of the list.

    Returns:
        [list]: a list of size n consisting of random elements.
    """    
    average_array = [0]*number
    for _ in range(5):
        random_array = [random.random() for _ in range(number)]
        average_array = [average_array[index] + random_array[index] for index in range(number)]
    
    average_array = [el/5 for el in average_array]

    return average_array

def generate_sorted_array(number: int, reverse: bool = False):
    """
    Generates an array of size n consisting of random elements
sorted in a given order.

    Args:
        number (int): size of the list.
        reverse (bool, optional): whether to sort in reverse order.
                                  Defaults to False.

    Returns:
        [list]: a list of size n consisting of random elements
                sorted in a given order.
    """    
    random_array = generate_array(number)
    random_sorted_array = sorted(random_array, reverse = reverse)
    return random_sorted_array

def generate_dense_array(number: int):
    """
    Generates an array of size n consisting of randomly chosen 
elements from the set {1, 2, 3}.

    Args:
        number (int): size of the list.

    Returns:
        [list]: a list of size n consisting of randomly chosen
                elements from the set {1, 2, 3}.
    """    
    ELEMENTS_SET = (1, 2, 3)
    
    average_array = [0]*number
    for _ in range(3):
        random_array = [random.choice(ELEMENTS_SET) for _ in range(number)]
        average_array = [average_array[index] + random_array[index] for index in range(number)]
    
    average_array = [min(ceil(el/3), 3) for el in average_array]

    return average_array

def generate_test_arrays():
    """
    Generates a list of lists to test on.

    Args:
        size_power ([int]): the power-value to determine size.

    Returns:
        list: a list of lists.
    """    

    return [generate_array, generate_sorted_array, generate_sorted_array, generate_dense_array]

if __name__ == '__main__':
    pass
