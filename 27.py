class Solution(object):
    def removeElement(self, nums, val):
        filtered = list(filter(lambda x: x != val, nums))

        for i in range(len(filtered)):
            nums[i] = filtered[i]

        return len(filtered)