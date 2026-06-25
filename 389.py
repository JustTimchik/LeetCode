class Solution(object):
    def findTheDifference(self, s, t):
        for b in t:
            if s.count(b) != t.count(b):
                return b