class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        # if no spaces, return full length
        if ' ' not in s:
            return length
        # iterate through the back
        for i in range(length - 1, -1, -1):
            # if its not space
            if s[i] != " ":
                # from current index, find space
                for x in range(i, -1, -1):
                    if s[x] == " ":
                        # if space is found i - x
                        return i - x
                # if not return i + 1
                return i + 1