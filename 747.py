class Solution(object):
    def dominantIndex(self, nums):
        st=sorted(nums)
        if st[-1]>=2*st[-2]:
            for i in range(len(nums)):
                if nums[i]==st[-1]:
                    return i
        return -1
