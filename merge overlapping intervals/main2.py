# The solution to this problem requires first sorting the intervals by their start times. Then we simply iterate through this sorted array, and do the following: if the result array is empty, append the current interval to the result array. Otherwise, check if the current interval should be merged with the last interval in the result array so far. If yes, modify the last interval in the result array to be the merged version of the 2 intervals. Otherwise, simply append the current interval to the results array.

def merge(intervals):
  result = []
  for start, end in sorted(intervals, key=lambda i: i[0]):
    # If current interval overlaps with the previous one, combine them
    if result and start <= result[-1][1]:
      prev_start, prev_end = result[-1]
      result[-1] = (prev_start, max(end, prev_end))
    else:
      result.append((start, end))
  return result

print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# [(1, 3), (4, 10), (20, 25)]

# The time complexity of this solution is O(N log N) due to the sorting. After the sorting, we are simply iterating over the array which takes linear time. The space complexity is O(N) for the results array.