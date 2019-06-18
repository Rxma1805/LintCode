class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        N = len(nums)
        if N == 1:
            return nums[0]
        for i in range(0,N,1):
            if i == 0 and nums[i] > nums[i+1]:
                return nums[i]
            elif i+1 == N:
                return nums[i]
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return nums[i]
            
            
            
