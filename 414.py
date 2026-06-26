class Solution(object):
    def thirdMax(self, nums):
        nums=sorted(set(nums))
        if len(nums)>=3:
            return nums[-3]
        elif len(nums)<3 and len(nums)>0:
            return nums[-1]
        else:
            return None
