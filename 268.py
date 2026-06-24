class Solution(object):
    def missingNumber(self, nums):
        nums=sorted(nums)
        i=0
        j=1
        if not nums or nums[0]!=0:
            return 0
        while j<len(nums):
            if (nums[i]+1)!=nums[j]:
                return nums[i]+1
            i+=1
            j+=1
        return nums[-1]+1
