"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if not root:
            return {}
        # write your code here
        if not root:
            return None
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        
        if left:
            tmp = left
            while tmp.right:
                tmp = tmp.right
            tmp.right = root.right
            root.right = root.left
            root.left = None
        return root
