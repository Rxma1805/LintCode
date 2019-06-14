class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        d = [[0 for row in range(m+1)] for col in range(n+1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    d[i+1][j+1] = d[i][j]+1
                else:
                    d[i+1][j+1] = max(d[i][j+1],d[i+1][j])
        return d[m][n]
