class Solution(object):
    def heightChecker(self, heights):
        srt=sorted(heights)
        l=0
        for i in range(len(heights)):
            if heights[i]!=srt[i]:
                l=l+1
        return l