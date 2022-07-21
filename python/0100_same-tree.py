# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            if p is None and q is None:
                return True
            if p and q is None:
                return False
            if p is None and q:
                return False
            if p.val != q.val:
                return False
            return same_tree(p.left, q.left) and same_tree(p.right, q.right)
        return same_tree(p,q)