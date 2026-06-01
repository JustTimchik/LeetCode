class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return 0
        max_length = 1
        max_string = s[0]
        for left in range(len(s)):
            for right in range(left + 1, len(s) + 1):
                if s[left:right] == s[left:right][::-1]:
                    if right - left > max_length:
                        max_length = right - left
                        max_string = s[left:right]
        return max_string