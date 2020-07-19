class Solution:
    def mp(self,grid,x,y):
        
        if x==self.r-1 and y==self.c-1:
            return grid[x][y]
        if not -1<x<self.r:
            return float('inf')
        if not -1<y<self.c:
            return float('inf')
        print(x,y)
        return grid[x][y]+min(self.mp(grid,x+1,y),self.mp(grid,x,y+1))
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.r=len(grid)
        self.c=len(grid[0])
        return self.mp(grid,0,0)
        