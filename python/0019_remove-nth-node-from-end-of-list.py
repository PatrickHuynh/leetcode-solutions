# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        cur = head
        prev = None
        new_head = head
        while cur is not None:
            if i >= n:
                if prev is None:
                    prev = head
                else:
                    prev = prev.next
            cur = cur.next
            i += 1
        if prev is None:
            new_head = head.next
        elif prev.next is None:
            prev.next = None
        else:
            prev.next = prev.next.next
        return new_head
            
