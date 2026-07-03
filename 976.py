class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        i,j,l=-3,-2,-1
        while i>=-len(nums):
            if nums[i]+nums[j]>nums[l]:
                return nums[i]+nums[j]+nums[l]
            i=i-1
            j=j-1
            l=l-1
        return 0