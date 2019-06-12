Create 最长回文字符串.py

627. Longest Palindrome
中文English
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Example
Example 1:

Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.
Notice
Assume the length of given string will not exceed 1010.

        
总长度减去无法成对的字符     
如果剩余无法成对的字符，则长度加1
    
