# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        dupes = set([head.val])
        n = head.next
        prev_n = head
        while n is not None:
            if n.val not in dupes:
                prev_n.next = n
                prev_n = n
            
            if n.next is None:
                if n.val in dupes:
                    prev_n.next = None
                
            dupes.add(n.val)
            n = n.next
        return head