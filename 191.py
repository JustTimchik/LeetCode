class Solution(object):
    def hammingWeight(self, n):
        s=bin(n)[2:]
        return s.count("1")