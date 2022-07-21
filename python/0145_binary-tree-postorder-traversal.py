# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder_traverse(root, nums):
            if root is None:
                return nums
            nums = postorder_traverse(root.left, nums)
            nums = postorder_traverse(root.right, nums)
            nums.append(root.val)
            return nums
        return postorder_traverse(root, [])
        