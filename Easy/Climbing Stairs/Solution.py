# Answer was taken from https://www.youtube.com/watch?v=Y0lT9Fck7qI
# Great explanation from the video
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        first, second = 1, 1
        for v in range(n - 1):
            temp = first
            first += second
            second = temp
        return first