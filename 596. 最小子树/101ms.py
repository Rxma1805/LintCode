"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    
    def findSubtree(self,root):
        import sys
        self.sums = sys.maxsize
        self.N = None
        self.find(root)
        return self.N
    
    def find(self, root):
        # write your code here
        if root == None:
            return 0
        left  = self.find(root.left)
        right = self.find(root.right)
        tmp = root.val + left +right
        if self.sums > tmp:
            self.N = root
            self.sums = tmp
        return tmp
        
