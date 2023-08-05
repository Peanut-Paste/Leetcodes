# Initially I solved it by bruteforce but the runtime is too long
# Went to look for answer which I understand which is this

class Solution:
    def longestPalindrome(self, s):
        def expand(l, r):
            # if left index is more than 0 and
            # right index is less than length of s and
            # left right s[index] is same
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        result = ""
        for i in range(len(s)):
            # this check for odd size eg. 'aba'
            sub1 = expand(i, i)
            if len(sub1) > len(result):
                result = sub1
            # check for even size eg. 'bb'
            sub2 = expand(i, i+1)
            if len(sub2) > len(result):
                result = sub2
        return result