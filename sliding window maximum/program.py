from collections import deque

def slidingWindowMax(nums: list[int], k: int):
    res = []
    queue = deque()
    l = 0
    for r in range(len(nums)):
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        
        queue.append(r)
        
        if queue[0] < l:
            queue.popleft()

        if r >= k - 1:
           res.append(nums[queue[0]])
           l += 1

    return res

print(slidingWindowMax([1,2,1,0,4,2,6], 3));

# debug
# 1 2 1 0 4 2 6
#             ^
#
# i = 6
# k = 3
# q [ 6 ]
# res [ 2, 2, 4, 4, 6 ]



# why this works:
# - we keep monotonically decreasing deque
# - we remove everything from the right, that is less than current
# - this allows to keep the current  maximum on the left of the queue
# - in deque, we keep indexes, not values!
# - when window shifts, we remove the left indice if it's out of bounds 
# - r and l means right bound and left bound
