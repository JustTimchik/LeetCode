class Solution(object):
    def isPalindrome(self, x):
        s=str(x)
        for i, a in enumerate(s):
            if a != s[len(s)-1-i]:
                state = False
            else: state = True
        return state