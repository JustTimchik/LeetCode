class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        max_length = 0
        left = 0
        set_chars = set()
        for right in range(len(s)):
            while s[right] in set_chars:
                set_chars.remove(s[left])
                left += 1
            set_chars.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
