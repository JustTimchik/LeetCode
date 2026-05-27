class Solution(object):
    def addTwoNumbers(self, l1, l2):
      num1 = 0
      num2 = 0
      l3 = []

      for x in l1:
          num1=num1+(10**l1.index(x))*x

      for x in l2:
          num2=num2+(10**l2.index(x))*x

      num3=num1+num2
      while num3>0:
          l3.append(num3%10)
          num3=num3//10
      return l3

s=Solution()
print(s.addTwoNumbers([2,4,3],[5,6,4]))
