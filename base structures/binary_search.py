def binarySearch(arr, num):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == num:
            return True
        elif arr[m] < num:
            l = m + 1
        elif arr[m] > num:
            r = m - 1
    return False


arr = [1, 4, 6, 8, 12]

for num in [6, 9]:
    print(binarySearch(arr, num))
