class Solution(object):
    def countBits(self, n):
        r=[]
        for i in range(n+1):
            t=bin(i)[2:]
            r.append(t.count("1"))
        return r
