class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            print(strs)
            d={}
            for x in strs:
                w=x
                x=''.join(sorted(x))
                
                if x not in d:
                    d[x]=[w]
                else:
                    d[x].append(w)
                
            
            return d.values()