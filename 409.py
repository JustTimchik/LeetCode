class Solution(object):
    def longestPalindrome(self, s):
        d = 0
        for c in set(s):
            cnt = s.count(c)
            d += cnt // 2 * 2
        if d == len(s):
          return d
        else:
          return d + 1