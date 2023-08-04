# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if not length:
            return None
        # get the mid node
        mid_node = length // 2
        # recursive, recusion will always create a mid node, with left, being till mid, and right being mid till
        return TreeNode(nums[mid_node], self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1:]))