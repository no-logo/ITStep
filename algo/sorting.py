def swap(array, index1, index2):
    if index1 >= 0 and index1 < len(array) and index2 >= 0 and index2 < len(array):
        if array[index1] == array[index2]:
            return
        array[index1], array[index2] = array[index2], array[index1]

def min(array, start, end):
    min = array[start]
    min_index = start
    i = start + 1

    while i < end:
        if min >= array[i]:
            min = array[i]
            min_index = i
        i += 1
    return min_index

def bublle_sort(array):
    n = len(array)
    while n > 1:
        swapped = False
        for i in range(n - 1):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                swapped = True
        if not swapped:
            break
        n -= 1
    return array

def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = min(array, i, n)
        swap(array, i, min_index)

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        x = array[i]
        j = i - 1
        while j >= 0 and array[j] >  x:
            array[j+1] = array[j]
            j -= 1
            array[j+1] = x
    return array