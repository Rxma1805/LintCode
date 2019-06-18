class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        N = len(A)
        if A == None:
            return []
        if k > N:
            return A
            
        index = self.binarySearchFirstIndex(0,N-1,A,target)
        result=[]
        
        left,right = index-1,index
        for _ in range(k):
            if left <0:
                result.append(A[right])
                right+=1
            elif right == N:
                result.append(A[left])
                left-=1
                
            elif A[right] - target >= target - A[left]:
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        return result
        
    def binarySearchFirstIndex(self,left,right,A,target):
        if right - left == 1 or right == left:
            if A[left] == target:
                return left
            elif A[right] == target:
                return right
            elif A[right] - target > target -  A[left]:
                return left
            else:
                return right
        mid = (left+right)//2
        if A[mid] < target:
            return self.binarySearchFirstIndex(mid+1,right,A,target)
        else:
            return self.binarySearchFirstIndex(left,mid,A,target)
