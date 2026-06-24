class Solution(object):
    def isAnagram(self, s, t):
        sorted_s="".join(sorted(s))
        sorted_t="".join(sorted(t))
        return sorted_s==sorted_t