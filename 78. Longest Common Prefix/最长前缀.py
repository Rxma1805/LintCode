class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs) == 0:
            return ""
        tmp = strs[0]
        
        for idx_s in range(1,len(strs)):
            src = tmp
            min_length = len(tmp)
            tmp = ''
            dest = strs[idx_s]
            if min_length > len(dest):
                min_length = len(dest)
                
            i=0
            while i < min_length and src[i] == dest[i]:
                tmp += src[i]
                i+=1
        return tmp
