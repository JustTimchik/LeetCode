class Solution(object):
    def uniqueOccurrences(self, arr):
        s_n=set(arr)
        s_o=set()
        for i in s_n:
            s_o.add(arr.count(i))
        return len(s_n)==len(s_o)
