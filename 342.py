class Solution(object):
    def isPowerOfFour(self, n):
        while n!=0 and n!=1:
            if n%4==0:
                n=n//4
            else:
                return False
        if n==0:
            return False
        if n==1:
            return True