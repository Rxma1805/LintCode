class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, A):
        # write your code here
        N = len(A) 
        return self.binarySearchFirstIndex(0,N-1,A,A[N-1])
    
    def binarySearchFirstIndex(self,left,right,A,target):
        if right - left == 1 :
            if A[left] > A[right]:
                return A[right]
            else:
                return A[left]
        mid = (left+right)//2
        if A[mid] <= target:
            return self.binarySearchFirstIndex(left,mid,A,target)
        else:
            return self.binarySearchFirstIndex(mid,right,A,target)
