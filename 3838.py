class Solution(object):
    def mapWordWeights(self, words, weights):
        dict = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alphabet)):
            dict[alphabet[i]] = weights[i]
        result =""
        for word in words:
            weight = 0
            for char in word:
                weight += dict[char]
            result += alphabet[26 - weight % 26 - 1 ]
        return result


