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
        a =  self.deep(root)
        return a != -1
      
        
    def deep(self,root):
        if not root:
            return 0
        left = self.deep(root.left)
        right = self.deep(root.right)
        # print(left,right,root.val)
        if abs(left - right) > 1 or left == -1 or right ==-1:
            return -1
        else:
            return max(left,right)+1
