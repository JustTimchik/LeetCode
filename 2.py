class Solution(object):
    def addTwoNumbers(self, l1, l2):

        num1 = 0
        num2 = 0
        power = 0

        curr = l1
        while curr:
            num1 += curr.val * (10 ** power)
            power += 1
            curr = curr.next

        power = 0
        curr = l2
        while curr:
            num2 += curr.val * (10 ** power)
            power += 1
            curr = curr.next

        num3 = num1 + num2

        dummy = ListNode(0)
        curr = dummy

        if num3 == 0:
            return ListNode(0)

        while num3 > 0:
            curr.next = ListNode(num3 % 10)
            curr = curr.next
            num3 //= 10

        return dummy.next