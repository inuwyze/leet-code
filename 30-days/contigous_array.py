class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        
        hash_map={}
        hash_map[0]=-1
        mx_subarr=0
        sms=0
        
        for i,x in enumerate(nums):
            if x==0:
                sms-=1
            else:
                sms+=1
            
            if sms in hash_map:
                s=i-hash_map[sms]
                mx_subarr=max(mx_subarr,s)
            else:
                hash_map[sms]=i
                
                
        return mx_subarr
        
        
