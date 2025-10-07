# a b c b a d
# a b b a d

def lps(s):
    resStart = 0    # alternatively: just resStr = ""
    resLen = 0

    def lps_helper(s, l, r):
        nonlocal resStart, resLen
        while l >= 0 and r < len(s) and s[l] == s[r]:
            curLen = r - l + 1
            if curLen > resLen:
                resStart = l
                resLen = curLen
            l -= 1
            r += 1

    for i in range(len(s)):
        # odd len  palindrome
        lps_helper(s, i, i)
        # even len palindrome
        lps_helper(s, i, i+1)

    return s[resStart:resLen + 1]


print(lps("abcbad"))
print(lps("abbad"))
