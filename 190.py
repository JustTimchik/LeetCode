class Solution(object):
    def reverseBits(self, n):
        n=bin(n)[2:]
        n=n.zfill(32)
        return int((n[::-1]),2)