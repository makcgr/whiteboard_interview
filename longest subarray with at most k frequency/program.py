# Find the length of a longest subarray with at most k frequency
#
# Input: nums = [1,2,3,1,2,3,1,2], k = 2
# Output: 6

from collections import defaultdict

def LongestSubarrayWithAtMostKFrequency(arr, k):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1

    counts = defaultdict(int) # frequency inside a window

    l = 0
    counts[arr[l]] = 1
    res  = 1
    for r in range(1, len(arr)):
        counts[arr[r]] += 1
        while counts[arr[r]] > k:
            counts[arr[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


arr, k = [1,2,3,1,2,3,1,2], 2
print(LongestSubarrayWithAtMostKFrequency(arr,k))

arr, k = [1,2,1,2,1,2,1,2], 1
print(LongestSubarrayWithAtMostKFrequency(arr,k))

arr, k = [5,5,5,5,5,5,5], 4
print(LongestSubarrayWithAtMostKFrequency(arr,k))

