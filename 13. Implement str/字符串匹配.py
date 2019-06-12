class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        if target == "":
            return 0
        if source == None or target == None:
            return -1
        ls = len(source)
        lt = len(target)
        if ls < lt:
            return -1
        for i in range(ls-lt+1):
            if source[i:lt+i] == target:
                return i
        return -1
