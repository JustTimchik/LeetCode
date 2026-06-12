class Solution(object):
    def deleteDuplicates(self, head):
        curr=head
        set1=set()
        while curr:
            set1.add(curr.val)
            curr=curr.next
        dummy=ListNode(0)
        curr=dummy
        set1=sorted(set1)
        for i in set1:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
