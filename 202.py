class Solution(object):
    def isHappy(self, n):
        s=set()
        while n not in s:
            s.add(n)
            n = sum(int(i) ** 2 for i in str(n))
            if n==1:
                return True
        return False
        
        