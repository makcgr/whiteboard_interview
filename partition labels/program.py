class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        lastIndices = [0] * 26

        for i, c in enumerate(s):
            lastIndices[ord(c)-ord('a')] = i

        res = []
        curLast = 0
        l = 0
        for r, c in enumerate(s):
            curLast = max(curLast, lastIndices[ord(c)-ord('a')])
            if r == curLast:
                res.append(r - l + 1);
                l = r+1
        return res

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
print(Solution().partitionLabels("eccbbbbdec"))



# why it works:
# 
# ababcbacadefegdehijhklij
#     ^ 
# with i=5, curLast = 8 (since a's last index in the string is 8)

#1) introduce hashtable / array of 26 positions: value=last indice of char, key: ord(c)-ord('a')
#2) maintain: curLast, l = left bound of cur partition ptr
#   for each character c and indice r: 
#       check if HIS last indice is greater than existing
#       if yes, overwrite the existing curLast
#       if current indice = curLast, we have our partition: 
#            add partition and update left ptr l
#   
#     
#
#
# lastIndices curIndices
# a: 8        a: 2
# b: 6        b: 4
# c: 5       c: ..
# d:
# e:
# f:
# g:
# h:
# i:
# j
# h
# k
# l


