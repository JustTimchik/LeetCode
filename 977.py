class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        a=[0]*n
        l,r=0,n-1
        p=n-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                a[p]=nums[l]**2
                l=l+1
            else:
                a[p]=nums[r]**2
                r=r-1
            p=p-1
        return a
