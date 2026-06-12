class Solution(object):
    def addBinary(self, a, b):
        a = int(a, 2)
        b = int(b, 2)
        c=a+b
        c = bin(c)[2:]
        return c