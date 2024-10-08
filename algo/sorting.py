def swap(array, index1, index2):
    if index1 >= 0 and index1 < len(array) and index2 >= 0 and index2 < len(array):
        if array[index1] == array[index2]:
            return
        array[index1], array[index2] = array[index2], array[index1]

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

