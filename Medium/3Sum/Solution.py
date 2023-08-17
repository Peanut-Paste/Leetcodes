class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, length = set(), len(nums)
        for i in range(length - 2):
            # mid will start 1 index from i
            mid = i + 1
            # end will start at end index
            end = length - 1
            while mid < end:
                current = nums[i] + nums[mid] + nums[end]
                # if current more than 0 then shift end
                if current > 0:
                    end -= 1
                # if lesser then, shift mid because list is sorted
                elif current < 0:
                    mid += 1
                else:
                    res.add((nums[i], nums[mid], nums[end]))
                    mid += 1
                    end -= 1
        return res