class Solution:
    def checker(self, left, right):
        # Same logic as Same Tree problem
        # Return true if both is null
        if not left and not right:
            return True
        # if either of them is null after first checker then return False
        # or val diff
        if not left or not right or left.val != right.val:
            return False
        # recursion, checking left's left with right's right and left's right with right's left
        return (self.checker(left.left, right.right) and self.checker(left.right, right.left))
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.checker(root.left, root.right)