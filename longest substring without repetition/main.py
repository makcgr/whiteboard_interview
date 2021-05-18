#
# Given a string, find the length of the longest substring without repeating characters.
#

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    cur_str = []
    max_len = 0    # recorded max_len for longest substring without repeating chars
    all_chars = list(s)
    
    for ix in range(len(all_chars)-1):
      for c_ix in range(ix, len(all_chars)-1):
        c = all_chars[c_ix]
        if c in cur_str:
          if len(cur_str) > max_len:
            max_len = len(cur_str)
          cur_str.clear()
        else:
          cur_str.append(c)

    if(max_len == 0):
      max_len = len(cur_str)
    return max_len


print(Solution().lengthOfLongestSubstring('abrkaabccdefghijjxxx'))
# 10
#print("Test")
