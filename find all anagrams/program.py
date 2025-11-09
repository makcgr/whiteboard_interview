# cbaebabacd   abc
#    ^
#  ^ 3 
#  1
#
# pCount:  sCount: 
# a: 1  c: 1
# b: 1  b: 1
# c: 1  a: 1
#
# 1) range(len(p)):
#    append pCount
#    append sCount
#
# for i in range (len(p), len(s):
#    update hashtable (remove latest)
#    if anagram(sCount = pCount): update result

def find_anagrams(s: str, p: str) -> list[int]:
    if len(s) < len(p):
        return []
    
    pCount, sCount = {}, {}
    res = []
    for i in range(len(p)):
        pCount[p[i]] = pCount.get(p[i], 0) + 1
        sCount[s[i]] = sCount.get(s[i], 0) + 1
    
    if pCount == sCount:
        res.append(0)
    l = 0
    for r in range(len(p), len(s)): # e.g. r from 3 to 9
        sCount[s[r]] = sCount.get(s[r], 0) + 1
        sCount[s[l]] -= 1
        if sCount[s[l]] == 0:
            sCount.pop(s[l])

        l += 1
        if pCount == sCount:
            res.append(l)

    return res


s = "cbaebabacd"
p = "abc"
print(find_anagrams(s, p))
