nums=[[4,4,4,0,0,0],
    [0,4,0,0,0,0],
    [0,4,4,0,0,0],
    [0,4,0,0,0,0],
    [0,0,0,4,0,0],
    [0,0,0,0,0,0]]

dir=[[0,1],[1,0],[-1,0],[0,-1]]

def dfs(x,y):
    nums[x][y]=0
    for xx,yy in dir:
        if -1<x+xx<6 and -1<y+yy<6: 
            if nums[x+xx][y+yy]:
                
                dfs(x+xx,y+yy)


dfs(0,0)
for x in nums:
    print(x)

