class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        final=0
       
        for x in shift:
            
            if x[0]:
                final-=x[1]
            else:
                final+=x[1]
            
        final%=len(s)
        
        
        
        return s[final:]+s[:final] if final else s
        
            
            