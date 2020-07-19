import math
nums=[2,3,4,5,6,7,8,9,10,11,12,13]
# nums=[2,3,4,5,6,7,8,9,10,11,12,13]

# print(len(nums)//2)
# print(len(nums))
mid=len(nums)//2
piv=nums[0]
l=0
u=len(nums)-1
x=0
while l<=u:
    
    print(mid,u,l)
    if nums[mid-1]>nums[mid]:
        print(mid)
        break
    if nums[mid]<piv:
        u=mid-1
    elif nums[mid]>piv:
        l=mid+1
    mid=int(math.ceil(u-l)/2+l)
    x+=1

if l>u:
    print('sorted')

