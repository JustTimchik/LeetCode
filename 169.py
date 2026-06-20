class Solution(object):
    def majorityElement(self, nums):
        s=set(nums)
        for i in s:
            sm=0
            for j in nums:
                if j==i:
                    sm=sm+1
            if sm > (len(nums)/2):
                return i
        return False
