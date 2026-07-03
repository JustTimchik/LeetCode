class Solution(object):
    def addToArrayForm(self, num, k):
        i=len(num)-1
        a=[]
        while i>=0 or k>0:
            if i>=0:
                k=k+num[i]
                i=i-1
            a.append(k%10)
            k=k//10
        return a[::-1]
