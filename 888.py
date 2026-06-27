class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        t=(sum(aliceSizes)-sum(bobSizes))//2
        for i in aliceSizes:
            for j in bobSizes:
                if i-j==t:
                    return i,j