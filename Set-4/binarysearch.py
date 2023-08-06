def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

input_array = [1, 2, 3, 4, 5, 6]
target_value = 4
output = binary_search(input_array, target_value)
print(output) 
