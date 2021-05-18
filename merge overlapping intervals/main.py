def merge(int1, int2):
  if (int1[0]<=int2[1] and int1[0]>=int2[0]])
  or (int2[0]<=int1[1] and int2[0]>=int1[0]]):
    return (int1[0] if int1[0]<int2[0] else int2[0],
            int1[1] if int1[1]>int2[1] else int2[1])
   

def merge(intervals):
  # Fill this in.
  # 
  # My algo: 
  # 1. First of all, sort them
  #    e.g. (1, 3), (5, 8), (4, 10), (20, 25)
  #         ->
  #         (1, 3), (4, 10), (5, 8), (20, 25)
  #    How to sort:
  #      Doing bubble sort N iterations from 0 to Z 
  #      where Z= N-iteration_num
  #      with each pass finding the biggest number 
  #      in positions from 0 to Z
  #      Comp cost = O(N)
  # 2. After sort:
  #     i = 0
  #     While i< len(intervals)-1 do:
  #       if new_interval = mergeable(intervals(i), intervals(i+1)):
  #          intervals(i) = new_interval     
  #          intervals.remove(intervals(i+1))
  #       else:
  #          i += 1
  #
  #       Comp cost = O(N) also.

# bubble sort for intervals
  n = len(intervals)
  for z=n-1 to 0:
    farthest_int = None
    for i=0 to z:
      if cur_farthest_int = None or intervals[i][0] > farthest_int[0]
        or intervals[i][0] = farthest_int[0] and intervals[i][1] > farthest_int[1]:    
        cur_farthest_int = intervals[i]
    intervals[z] = farthest_int

 
# space complexity: O(1), no additional complexity
  
# after sort: merging while it's possible
i = 0
While i< len(intervals)-1 do:
  if new_interval = mergeable(intervals(i), intervals(i+1)):
      intervals(i) = new_interval     
      intervals.remove(intervals(i+1))
  else:
      i += 1
 

print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# [(1, 3), (4, 10), (20, 25)]