class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=len(stones)
        while(s>1):
            y=max(stones)
            stones.remove(y)
            x=max(stones)
            stones.remove(x)
            if y==x:
                s-=2
            else:
                s-=1
                stones.append(y-x)
        if stones:       
            return stones[0]
        else:
            return 0