class Solution(object):
    def addBinary(self, a, b):
        if b>a:
            a,b=b,a
        while len(a)!=len(b):
            b="0"+b
        i=len(a)-1
        c=""
        addex=0
        while i>-1:
            if addex==0:
                if a[i]=="1" and b[i]=="1":
                    if i==0:
                        c="10"+c
                    else:
                      c="0"+c
                      addex=1
                elif a[i]=="0" and b[i]=="0":
                    c="0"+c
                else:
                    c="1"+c
            else:
                if a[i]=="1" and b[i]=="1":
                    if i==0:
                      c="11"+c
                    else:
                      c="1"+c
                      addex=1
                elif a[i]=="0" and b[i]=="0":
                    c="1"+c
                    addex=0
                else:
                    if i==0:
                      c="10"+c
                    else:
                      c="0"+c
            i-=1
        return c

