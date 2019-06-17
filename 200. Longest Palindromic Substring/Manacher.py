class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        s = '#'+'#'.join(s)+'#'
        pos = 0
        maxRight = 0 #最右侧
        maxLength = 0#长度
        maxPos=0
        N = len(s)
        Rl = [0] * N
        for i in range(N):
            if i < maxRight:
                Rl[i] = min(Rl[2*pos-i],maxRight-i)
            else:
                Rl[i] = 1
                
            while  i+Rl[i] < N and i-Rl[i] >= 0 and s[i+Rl[i]] == s[i-Rl[i]]:
                Rl[i]+=1
                
            if maxRight < i + Rl[i] -1:
                maxRight = i + Rl[i] -1
                pos=i
            if maxLength < Rl[i]:
                maxPos=i
                maxLength=Rl[i]-1
                
            
        tmp = s[maxPos-maxLength:maxLength+maxPos+1] 
        return tmp.replace('#','')
                
                
            
        
