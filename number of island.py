class Solution:
    def ok(self):
        print(ok)
    
    def dfs(self,x,y,nums)->None:
        nums[x][y]='0'
        # print(nums)
        dir=[[0,1],[1,0],[-1,0],[0,-1]]
        for xx,yy in dir:
            if -1<x+xx<self.row and -1<y+yy<self.col: 
                if nums[x+xx][y+yy]=='1':

                    dfs(x+xx,y+yy)
        
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
            self.ok()
            if not grid:
                return 0
            
            row=len(grid)
            col=len(grid[0])
            count=0
            for i,x in enumerate(grid):
                for j,y in enumerate(x):
                    print(y)
                    if y=='1':
                        print(3)
                        count+=1
                        
                        self.dfs(i,j,grid)
            print(grid)
            print(row,col)
                        
            return count