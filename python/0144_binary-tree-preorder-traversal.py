# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder_traverse(root, nums):
            if root is None:
                return nums
            nums.append(root.val)
            nums = preorder_traverse(root.left, nums)
            nums = preorder_traverse(root.right, nums)
            return nums
        return preorder_traverse(root, [])