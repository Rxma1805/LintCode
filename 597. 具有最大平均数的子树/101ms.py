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
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.mean=float('-inf')
        self.N=None
        self.find(root)
        return self.N
        
    def find(self,root):
        
        if not root:
            return (0,0)#  sums,size
            
        left  = self.find(root.left)
        right = self.find(root.right)
        
        sums,size = left[0] + right[0] + root.val,left[1]+right[1]+1
        if self.mean < sums/size:
            self.mean=sums/size
            self.N=root
        return sums,size
            
        
        
        
