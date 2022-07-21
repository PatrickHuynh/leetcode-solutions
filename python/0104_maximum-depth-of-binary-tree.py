# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def next_depth(root, n):
            if root is None:
                return n
            return max(next_depth(root.left, n), next_depth(root.right, n)) + 1
        return next_depth(root, 0)