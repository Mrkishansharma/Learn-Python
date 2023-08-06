
# bubble sort 

arr = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(arr) : 
    for i in range(len(arr)-1) :
        for j in range(len(arr)-2) :
            if arr[j] > arr[i] :
                arr[i], arr[j] = arr[j], arr[i]
    return arr


print(bubble_sort(arr))
