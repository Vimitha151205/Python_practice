def selection_sort(array,size):
    for i in range(size-1):
        min_index = i
        for j in range(i+1,size):
            if array[j]<array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index],arr[i]
arr = [-2,45,0,11,-9,88,-97,-202,747]
size = len(arr)
selection_sort(arr,size)
print(arr)
                                                   
