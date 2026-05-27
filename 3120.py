class Solution(object):
    def numberOfSpecialChars(self, word):
        k = 0
        
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in word and c.upper() in word:
                k += 1
                
        return k