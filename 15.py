class Solution(object):
    def threeSum(self, nums):
        solution_set=[]
        for i in range (len(nums)):
            for j in range (len(nums)):
                for k in range (len(nums)):
                    if (i!=j and j!=k and i!=k) and (nums[i]+nums[j]+nums[k]==0):
                        if tuple(sorted((nums[i],nums[j],nums[k]))) not in solution_set:
                          solution_set.append(tuple(sorted((nums[i],nums[j],nums[k]))))
        return solution_set
