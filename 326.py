class Solution(object):
    def isPowerOfThree(self, n):
        while n!=0 and n!=1:
            if n%3==0:
                n=n//3
            else:
                return False
        if n==0:
            return False
        if n==1:
            return True