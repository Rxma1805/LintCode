"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        a =  self.deep(root.left)
        b = self.deep(root.right)
        if abs(a-b) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right) 
      
        
    def deep(self,root):
        if not root:
            return 0
        left = self.deep(root.left)
        right = self.deep(root.right)
        return max(left,right)+1
        
