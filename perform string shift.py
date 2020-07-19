class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        shft={1:0,0:0}
       
        for x in shift:
            
            shft[x[0]]+=x[1]
            
        final=(shft[0]-shft[1])%len(s)
        
        
        
        return s[final:]+s[:final] if final else s
        
            
            