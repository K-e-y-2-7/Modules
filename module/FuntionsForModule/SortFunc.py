'''
Sorting Algorithms
==================

'''

def sort_function(list_sort: list) -> list:
    '''Return a sorted collection'''

    if len(list_sort) <= 1:
        return list_sort

    base = list_sort[0]
    left = [element for element in list_sort if element < base]
    middle = [element for element in list_sort if element == base]
    right = [element for element in list_sort if element > base]

    return sort_function(left) + middle + sort_function(right)
