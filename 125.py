class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        t = "".join(c for c in s if c.isalnum())
        m=len(t)//2
        if len(t)%2==1:
            if t[:m][::-1]==t[m+1:]:
                return True
        else:
            if t[:m][::-1]==t[m:]:
                return True
        return False
