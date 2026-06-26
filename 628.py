class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        mx=nums[-1]*nums[-2]*nums[-3]
        nx=nums[0]*nums[1]*nums[-1]
        xx=nums[0]*nums[1]*nums[2]
        mx=max(mx,nx)
        xx=max(mx,xx)
        return xx