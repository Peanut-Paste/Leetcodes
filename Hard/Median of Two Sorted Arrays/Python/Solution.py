class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Combined arrays
        new_list = nums1 + nums2
        # sort it in ascending
        new_list.sort()
        length = len(new_list)
        # if length is divisible by 2
        if length % 2 == 0:
            # return mid 2 values / 2
            return (new_list[int(length / 2) - 1] + new_list[int(length / 2)]) / 2
        else:
            # else just return middle value
            return new_list[int(length / 2)]