# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder_traverse(root, nums):
            if root is None:
                return nums
            nums = inorder_traverse(root.left, nums)
            nums.append(root.val)
            nums = inorder_traverse(root.right, nums)
            return nums
        return inorder_traverse(root, [])
        