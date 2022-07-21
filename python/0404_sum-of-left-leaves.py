# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_left_leaves(root, is_left_leaf, n):
            if root is None:
                return 0
            elif root.left is None and root.right is None:
                if is_left_leaf:
                    return root.val
                else: 
                    return 0
            return sum_left_leaves(root.left, True, n) + sum_left_leaves(root.right, False, n)
        return sum_left_leaves(root, False, 0)
            