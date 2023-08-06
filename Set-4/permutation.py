
def swap(arr, a, b) :
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def permute(arr, i):
  if i>=len(arr) :
    print(arr)
    return
  for j in range(i,len(arr)) :
    swap(arr, i, j)
    permute(arr, i+1)
    swap(arr, i, j)


arr = ['a','b','c']

permute(arr, 0)
