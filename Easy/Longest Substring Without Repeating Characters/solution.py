class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if length of string is 1 then return 1
        if len(s) == 1: 
            return 1
        count=0 
        new=''
        for i in s:
            # if i is not in new then add it to the string
            if i not in new:
                new+=i
            # if it is not new, slice out the current letter in the sub string
            else:
                new=new[new.index(i)+1:] + i
            # if current len of new substring is bigger, then replace count
            if len(new) > count:
                count=len(new)
        return count