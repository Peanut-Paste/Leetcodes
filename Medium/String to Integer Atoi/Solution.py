# this was pretty easy because I have to code this in c without any library
# for my 42 Singapore class
class Solution:
    def myAtoi(self, s: str) -> int:
        i, total, length, is_neg = 0, 0, len(s), False
        # move index if is space
        while i < length and s[i].isspace():
            i += 1
        # optional because it might not have - or +
        if i < length and (s[i] is '-' or s[i] is '+'):
            # if it is -, set is neg to true
            if s[i] == '-':
                is_neg = True
            i += 1
        # while it is numerical, it might be 123a, so it stops at 123
        while i < length and s[i].isnumeric():
            total = total * 10 + int(s[i])
            i+= 1
        # if bigger than 32 bits, return the max size for 32 bits
        if total > 2 ** 31 - 1 or total < -2 ** 31:
            if is_neg:
                return -2 ** 31
            else:
                return 2 ** 31 - 1
        # if is neg, then return total in negative.
        if is_neg:
            return total * -1
        return total