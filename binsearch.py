# nums=[14,15,16,17,1,2,3,4,5,6,7,8,9,10,11,12,13]
# nums=[14,1,2,3,4,5,6,7,8,9,10,11,12,13]

nums=[2,3,4,5,6,7,8,9,10,11,12,13,1]
# nums=[2,3,4,5,6,7,8,9,10,11,12,13]

# print(len(nums)//2)
# print(len(nums))
mid=len(nums)//2
piv=nums[0]
l=0
u=len(nums)-1

while(1):
    # print(mid) 
    if nums[mid]<piv:
        if nums[mid-1]>nums[mid]:
            print(mid)
            break
        mid-=(mid-l)//2
        u=mid-1
       
    elif nums[mid]>piv:
        if nums[mid+1]<piv:
            print(mid+1)
            break
        elif mid+1==u:
            print('sorted')
            break
        mid+=(u-mid)//2
   