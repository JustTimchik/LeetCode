class Solution(object):
    def numOfStrings(self, patterns, word):
        l=0
        for i in patterns:
            if i in word:
                l=l+1
        return l