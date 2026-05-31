class Solution(object):
    def removeDuplicates(self, nums):
        nums_set = set(nums)
        nums_sorted = sorted(nums_set)
        for i in range(len(nums_sorted)):
            nums[i] = nums_sorted[i]
        return len(nums_set)
