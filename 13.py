class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = ""
        if not strs:
            return prefix
        for str in strs:
            for i in range(len(str)):
                if i >= len(prefix) or str[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
            if not prefix:
                return prefix
        return prefix