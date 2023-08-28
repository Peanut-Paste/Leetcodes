class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through list with enumerate
        for i, v in enumerate(nums):
            # x will always be ahead of i
            for x in range(i + 1, len(nums)):
                # if sums add ups as same value as the target
                if (v + nums[x]) == target:
                    return [i, x]