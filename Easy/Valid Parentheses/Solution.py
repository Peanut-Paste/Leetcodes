class Solution:
    def isValid(self, s: str) -> bool:
        # if s == 1 return False
        if len(s) == 1:
            return False
        # Init dictionary of brackets, count of strs and a new str
        strs, c, bracket = "", -1, {"{": "}", "(": ")", "[": "]"}
        for v in s:
            # if v not in bracket values e.g {, (, [
            if v not in bracket.values():
                # at it to new string
                strs = strs + v
                # count follow the index of latest new letter in new string
                c += 1
            else:
                # if the count is less than 0 e.g "})" or v not == to the counter part of latest letter
                if c < 0 or v != bracket[strs[c]]:
                    return False
                else:
                    # remove the latest letter
                    strs = strs[:c]
                    # move index
                    c -= 1
        # if c is not -1 meaning new strs still has letter
        if c != -1:
            return False
        return True