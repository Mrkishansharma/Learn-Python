def find_missing_number(nums):
    n = len(nums)
    natural_sum = n * (n + 1) // 2
    arr_sum = sum(nums)
    missing_number = natural_sum - arr_sum
    return missing_number

numbers = [3, 0, 2, 1, 5,6]
missing_number = find_missing_number(numbers)
print(missing_number)   