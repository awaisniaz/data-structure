def uniqueElement(arr):
    k = 1
    for i in range(1, len(arr)):
     if arr[i] != arr[k - 1]:
        arr[k] = arr[i]
        k += 1
    return arr[0:k]
print(uniqueElement([1, 2, 2, 3, 4, 4, 5]))