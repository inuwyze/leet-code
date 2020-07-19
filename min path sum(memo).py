def memo(self,func):
        mem={}
        def helper(grid,x,y):
            print('helper')
            if not (x,y) in mem:
                mem[(x,y)]=func(grid,x,y)
                
            return mem[tuple(x,y)]
        return helper
    
    def dfs(self,grid,x,y):
        print('dfs')
        if x+y==self.row+self.col-2:
            return grid[x][y]
        if -1<x<self.row:
            return float('inf')
        if -1<y<self.col:
            return float('inf')
        return grid[x][y] +min(self.dfs(grid,x+1,y),self.dfs(grid,x,y+1))
    
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.dfs=self.memo(self.dfs)
        return self.dfs(grid,0,0)