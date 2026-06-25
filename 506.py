class Solution(object):
    def findRelativeRanks(self, score):
        srtd=sorted(score)
        dt={}
        ans=[]
        for i,v in enumerate(srtd):
            n=len(srtd)-i
            if n==1:
                dt[v]="Gold Medal"
            elif n==2:
                dt[v]="Silver Medal"
            elif n==3:
                dt[v]="Bronze Medal"
            else:
                dt[v]=str(n)
        for i in score:
            ans.append(dt[i])
        return ans
