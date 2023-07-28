class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target is already in nums, return the index of it
        if target in nums:
            return nums.index(target)
        # if the min of the list is more than target, target will be index 0
        elif min(nums) > target:
            return 0
        else:
            # a loop that will decrease nums to find the highest before target, return the index of it and add one to it
            while target not in nums:
                target -= 1
            return nums.index(target) + 1