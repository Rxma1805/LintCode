class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if len(nums) ==0:
            return -1
        return self.Binsearch(0,len(nums)-1,nums,target)
        
    def Binsearch(self,left,right,A,target):
        if left == right or (right-left == 1):
            if  A[right] == target:
                return  right
            elif A[left] == target:
                return  left
            
            else:
                return -1
        
        idx = (left+right)//2
        if target < A[idx]:
            return self.Binsearch(left,idx-1,A,target)
        elif target > A[idx]:
            return self.Binsearch(idx+1,right,A,target)
        else:
            return self.Binsearch(idx,right,A,target)
           
