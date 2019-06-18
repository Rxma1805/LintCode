class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, i):
        # write your code here
        if i == 0:
            return 1
        elif i<0:
            n = -i
        else:
            n = i
        
        res=1
        
        while n != 1:
            if n % 2 != 0:
                res *= x
            n = n >> 1
            x = x*x
        
        return 1/(res*x)  if i <0 else res*x
