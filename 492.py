class Solution(object):
    def constructRectangle(self, area):
        w = int(area ** 0.5)
        while w > 0:
            if area % w == 0:
                l = area // w
                return [l, w]
            w -= 1