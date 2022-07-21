"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return self.__preorder(root, [])
    
    def __preorder(self, root, vals):
        if root is None:
            return vals
        vals.append(root.val)
        for n in root.children:
            vals = self.__preorder(n, vals)
        return vals
        