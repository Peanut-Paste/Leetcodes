# Not the most optimized code, but it works
class Solution:
    def mySqrt(self, x: int) -> int:
        # If x = 0 return
        if x == 0:
            return 0
        else:
            i = 1
            # if i is lesser or equal to x try to find potential answer
            while i <= x:
                # if i * i = x, then we found the answer
                if i * i == x:
                    return i
                # if it went over, then the previous i, will be the rounded down num
                elif i * i > x:
                    return i - 1
                i += 1
        # if it did not find any answer, use the last i - 1 as the answer
        return i - 1