class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        s = s.lower()
        i=0
        j=len(s)-1
        while i < j:
            if not s[i].isalpha() and not s[i].isdigit():
                i+=1
                continue
            if not s[j].isalpha() and not s[j].isdigit():
                j-=1
                continue
            if s[i] != s[j]:
                return False
            else:
                i+=1
                j-=1
        return True
