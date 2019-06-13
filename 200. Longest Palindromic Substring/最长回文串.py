class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        leng=0
        idx = 0
        for i in range(len(s)):
            tmpLength =  self.getSublongestPalindrome(s,i,i)
            if tmpLength > leng:
                leng = tmpLength
                idx = i
                
        for i in range(len(s)):
            tmpLength =  self.getSublongestPalindrome(s,i,i+1)
            if tmpLength > leng:
                leng = tmpLength
                idx = i
        
        if leng % 2 ==0:
            start = idx-leng//2+1
            end = idx+leng//2+1
            return s[start:end] 
        else:
            start = idx-leng//2
            end = idx+leng//2+1
            return s[start:end] 
    
    
    def getSublongestPalindrome(self,s,left,right):
        leng=0
        while left>=0 and right < len(s):
            if s[left] != s[right]:
                break
            if left == right:
                leng += 1
            else:
                leng += 2
            left-=1
            right+=1
        return leng
