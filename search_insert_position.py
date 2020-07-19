class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo,hi,mid=0,len(nums)-1,(len(nums)-1)//2
        if not nums: return 0
        if target<nums[0]:return 0
        if target>nums[-1]:return len(nums)
            
        while lo<=hi:
            if nums[mid]==target:return mid
            if nums[mid]>target:
                hi=mid-1
            else:
                lo=mid+1
            mid=(hi+lo)//2
        
        return mid+1