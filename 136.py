class Solution(object):
    def singleNumber(self, nums):
        nums=sorted(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i+1]:
                continue
            else:
                return nums[i]
        return nums[len(nums)-1]
