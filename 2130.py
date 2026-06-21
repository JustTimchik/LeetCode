class Solution(object):
    def pairSum(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        first = head
        second = prev
        ans = 0
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next
        return ans