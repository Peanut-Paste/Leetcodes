# Deploying the same method as 3Sum
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the input list
        nums.sort()
        length = len(nums)
        # Create a infinite int variable
        lowest, abs_lowest = float('inf'), float('inf')
        for i in range(length - 2):
            # mid start after current index
            mid = i + 1
            end = length - 1
            while mid < end:
                # get current value
                current = nums[i] + nums[mid] + nums[end]
                # convert it to positive to compare, getting the lower distance away from target
                if abs(current - target) < abs_lowest:
                    # make it so that it can be compared
                    abs_lowest = abs(current - target)
                    # store the original int in lowest
                    lowest = current
                # since sorted, if current more then target, then move end to left
                if current > target:
                    end -= 1
                # if it is lower, then mid needs to move to right
                elif current < target:
                    mid += 1
                else:
                # if found target, then return current
                    return current
        # if nothing is found, then return the lowest
        return lowest