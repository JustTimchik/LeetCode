class Solution(object):
    def kWeakestRows(self, mat, k):
        rows = []
        for i in range(len(mat)):
            rows.append((mat[i].count(1), i))
        rows.sort()
        ans = []
        for i in range(k):
            ans.append(rows[i][1])
        return ans