class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=iter(t)
        for x in s:
            try:
                while next(i)!=x:
                    continue
            except StopIteration:
                return False
            
        return True
            