# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is null, return 0
        if not root:
            return 0
        # if not null, count will always be 1
        count = 1
        # recursion to add the max between left and right node
        count += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return count