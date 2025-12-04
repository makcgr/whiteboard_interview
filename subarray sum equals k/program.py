# [1, 1, 1] k=2
#   ^  ^
#      ^  ^
 
# [1, -1, 1, 1, 1, 1] k=3
#            i^
#   ---s------ question: s == k?
#
#              Other take: does s-k exist in array?
#                          (If it does,  s - (s - k) gives k
#
# e.g.
# [1, 2, 3, 1, 2, 1] k = 3                  HASHMAP {SUM : TIMES_FOUND}
#                       sum=0               {0:1} "zero sum is found once" (for edge case)
#  ^                i=0 sum=1   sum-k=-2    {0:1, 1:1}
#     ^             i=1 sum=3   sum-k=1     {0:1, 1:1, 3:1} !FOUND sum-k! (res+=1) 
#        ^          i=2 sum=6   sum-k=3     {0:1, 1:1, 3:1, 6:1} !FOUND sum-k! (res+=1)
#           ^       i=3 sum=7   sum-k=4     {0:1, 1:1, 3:1, 6:1, 7:1} (res+=1) 
#              ^    i=4 sum=9   sum-k=6     {0:1, 1:1, 3:1, 6:1, 7:1, 9:1} !FOUND sum-k! (res+=1)  
#                 ^ i=5 sum=10  sum-k=7     {0:1, 1:1, 3:1, 6;1, 7:1, 9:1, 10:1} !FOUND sum-k! (res+=1) 
# keep "running" sum in hashmap (how many times it appeared, could be several due to neg values)
# before adding each new sum to hashmap: check sum-k exists in hashmap => if so, add TIMES_FOUND to result
# ! NOTE ! keep {0:1} in hashmap to handle the case when sum-k equals 0
# Why this works? Because EACH time we found another sum-k in HM, it means, we have found yet another subarray for our total result! 
def subarraySumEqK(nums: list[int], k: int) -> int:
    res = 0
    prefixSums = { 0: 1 } # to handle border case sum-k=0
    curSum = 0 # sum
    for num in nums:
        curSum += num
        if prefixSums.get(curSum - k, 0):
            res += 1
        prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
    return res

print(subarraySumEqK([1, 2, 3, 1, 2, 1], 3))
