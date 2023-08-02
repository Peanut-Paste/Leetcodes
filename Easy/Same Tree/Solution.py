class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both nodes are null then return True
        if not p and not q:
            return True
        # if p is null or q is null after the check above then it can only means
        # only one of them is null
        # it also checks for diff val
        if not p or not q or p.val != q.val:
            return False
        # recursion call if all is good
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))