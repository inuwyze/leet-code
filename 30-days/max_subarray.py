class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if(nums[0]<0):
            cs=nums[0]
            bs=nums[0]
        else:
            cs=0
            bs=0
        i=1
        for x in nums:
            bs=max(bs,cs)
            cs=max(x,cs+x)
            print(cs)
          
        bs=max(bs,cs)    
        return bs
