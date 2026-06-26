class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        l=[]
        st=sorted(nums)
        for i in nums:
            l.append(st.index(i))
        return l
