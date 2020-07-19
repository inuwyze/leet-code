class Solution:
    def memo(self,func):
        mem={}
        def helper(grid,x,y):
            # print('helper')
            if not (x,y) in mem:
                mem[(x,y)]=func(grid,x,y)
                
            return mem[(x,y)]
        return helper
    
    def dfs(self,grid,x,y):
        # print('dfs')
        # print(x,y)
        if x==self.row-1 and y==self.col-1:
            return grid[x][y]
        if not -1<x<self.row:
            return float('inf')
        if not -1<y<self.col:
            return float('inf')
        return grid[x][y] +min(self.dfs(grid,x+1,y),self.dfs(grid,x,y+1))
    
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.row=len(grid)
        self.col=len(grid[0])
        self.dfs=self.memo(self.dfs)
        return self.dfs(grid,0,0)