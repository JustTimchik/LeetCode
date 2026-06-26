class Solution(object):
    def arrayPairSum(self, nums):
        nums=sorted(nums)
        i=len(nums)-1
        sm=0
        while i>0:
            sm=sm+nums[i-1]
            i=i-2
        return sm