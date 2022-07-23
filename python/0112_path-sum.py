# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sum_path(root, runsum, target):
            runsum += root.val
            if not root.left and not root.right:
                return runsum == target
            left = False
            right = False
            if root.left:
                left = sum_path(root.left, runsum, target)
            if root.right:
                right = sum_path(root.right, runsum, target)
            return left or right
        
        if root:
            return sum_path(root, 0, targetSum)
        else:
            return False