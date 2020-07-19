class Solution:
    def mul(self,nums):
        a=1
        for x in nums:
            a*= x if x!=0 else 1
        return a
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ml=0
        if nums.count(0)>1:
            return [0 for x in nums]
        elif nums.count(0)==1:
            ml=self.mul(nums)
            return [0 if x!=0 else ml for x in nums]
        else:
            ml=self.mul(nums)
            return [ml//x for x in nums]
