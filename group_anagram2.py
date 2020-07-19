from collections import defaultdict

def groupAnagrams( strs):
        
        d=defaultdict(list)
        for x in strs:
            w=x
            x=''.join(sorted(x))
            
            
            d[x].append(w)
            
        
        return d.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))