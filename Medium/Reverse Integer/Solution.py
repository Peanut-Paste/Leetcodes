class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        # check if neg, change to positive
        if x < 0:
            is_neg = True
            x *= -1
        # reverse the string and convert to string
        res = int((str(x)[::-1]))
        # if neg then make it negative
        if is_neg:
            res *= -1
        # if more than 32 bits integer, return 0
        if res > 2147483647 or res < -2147483648:
            return 0
        return res