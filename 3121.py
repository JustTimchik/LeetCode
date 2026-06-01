class Solution(object):
    def numberOfSpecialChars(self, word):
        k = 0
        last = {}
        for c in "abcdefghijklmnopqrstuvwxyz":
            for i,x in enumerate(word):
                if x == c:
                    last[c] = i
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in word and c.upper() in word:
                if last[c] < word.index(c.upper()):
                    k += 1
        return k