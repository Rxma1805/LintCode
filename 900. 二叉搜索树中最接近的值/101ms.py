"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        cnt = float('inf')
        val = 0
        while root:
            if abs(target - root.val) < cnt:
                cnt = abs(target - root.val)
                val = root.val
            if target == root.val:
                return target
            elif target >= root.val:
                root = root.right
            else:
                root = root.left
                
        return val
                
