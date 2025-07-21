def longest_increasing_subsequence_v1_recursive(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return 1

    max_ending_here = 0
    for i in range(1, len(arr)):     
        ending_at_i = longest_increasing_subsequence(arr[:i])
        if arr[-1] > arr[i-1] and ending_at_i + 1 > max_ending_here:
            max_ending_here = ending_at_i + 1
    return max_ending_here

def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range (i):
            if arr[i]>arr[j]:
                cache[i]=max(cache[i], cache[j]+1)
    return max(cache)


arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence_v1_recursive(arr)) # exponential O(2^N)
# 6
print(longest_increasing_subsequence(arr)) # O(N^2)
# 6