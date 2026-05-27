class Solution(object):
  def twoSum(self, nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in num_dict:
            return (num_dict[num2], i)
        num_dict[num] = i
