# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # Find next smallest element
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # Swap with current element
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        #temp = arr[i]
        #arr[i] = arr[smallest_index]
        #arr[smallest_index] = temp

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp: 
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr