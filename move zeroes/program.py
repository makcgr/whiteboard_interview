def moveZeroes(arr):
    l = 0
    for r in range(len(arr)):
        if arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
    return arr

def moveZeroes2(arr):
    wi = 0 # write index
    for num in arr:
        if num:
            arr[wi] = num
            wi += 1
    while wi < len(arr):
        arr[wi] = 0
        wi += 1
    return arr


arr = [0,0,1,2,0,5]  # 1 2 5 0 0 0
print(moveZeroes(arr))
print(moveZeroes2(arr))
