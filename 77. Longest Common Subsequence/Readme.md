77. Longest Common Subsequence
中文English
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

样例
说明
What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm



if A[i] == B[j]:    
   dp[i+1][j+1] = dp[i][j] + 1    
else:    
  dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])    
