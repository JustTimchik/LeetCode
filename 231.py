class Solution(object):
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        while n!=1 and n!=0:
            if n%2==0:
                n=n//2
            else:
                return False
        if n==1:
            return True
