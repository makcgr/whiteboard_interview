def FindMinimum(arr):
    l, r = 0, len(arr)-1
    while l < r:
        if arr[l] < arr[r]:
            return arr[l]
        mid = l + (r - l) // 2
        if arr[mid] == arr[r]:
            return arr[r]
        if arr[mid] > arr[l]:
            l = mid+1
        else:
            r = mid
    return arr[l]


arr = [7, 8, 1, 2, 3, 4, 5, 6]
result = FindMinimum(arr)
print(result)
