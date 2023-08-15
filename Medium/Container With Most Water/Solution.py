# I used the closing in method.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # if len = 2, there's no area to multiply, just return the min height
        if len(height) == 2:
            return min(height[0], height[1]) 
        highest, end, start, current = 0, len(height) - 1, 0, 0
        while start < end:
            # current capacity of min height * the area (difference in index)
            current = min(height[start], height[end]) * (end - start)
            if current > highest:
                highest = current
            # if start is higher than end then we shift end nearer
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return highest