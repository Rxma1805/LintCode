class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid :
            return 0
        m = len(grid)
        n = len(grid[0])
        numland = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numland+=1
                    self.dfs(grid,i,j)
        return numland
        
        
        
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i >=len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] ==1:
            grid[i][j] = 0
            self.dfs(grid,i-1,j)
            self.dfs(grid,i+1,j)
            self.dfs(grid,i,j-1)
            self.dfs(grid,i,j+1)
