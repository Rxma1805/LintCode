class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        un_pair = list()
        for c in s:
            if c not in un_pair:
                un_pair.append(c)
            else:
                un_pair.remove(c)
        if len(un_pair) != 0:
            return len(s) - len(un_pair)+1
        else:
            return len(s) - len(un_pair)
        
