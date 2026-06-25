class Solution(object):
    def intersect(self, nums1, nums2):
        its=set()
        rslt=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                its.add(nums1[i])
        for j in its:
            a1=0
            b1=0
            for a in nums1:
                if a==j:
                    a1=a1+1
            for b in nums2:
                if b==j:
                    b1=b1+1
            a1=min(a1,b1)
            rslt.extend([j]*a1)
        return rslt
