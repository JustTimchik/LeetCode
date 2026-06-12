class Solution(object):
    def plusOne(self, digits):
        i=len(digits)-1
        last=len(digits)-1
        if digits[i]<9:
            digits[i]=digits[i]+1
        else:
            while digits[i]==9:
                digits[i]=0
                i=i-1
                last=last-1
            if last==-1:
                digits.insert(0,1)
            else:
                digits[last]=digits[last]+1
        return digits