# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a = ahead = ListNode(0)
        b = bhead = ListNode(0)
        while head:
            if head.val < x:
                a.next = head
                a = a.next
            else:
                b.next = head
                b = b.next
            head = head.next
        b.next = None
        if a == ahead:
            head = bhead.next
        else:
            a.next = bhead.next
            head = ahead.next
        return head