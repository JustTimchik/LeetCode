class Solution(object):
    def largestAltitude(self, gain):
        alt=[0]*(len(gain)+1)
        for i in range(len(gain)):
            alt[i+1]=alt[i]+gain[i]
        m=alt[0]
        for j in alt:
            if j>m:
                m=j
        return m