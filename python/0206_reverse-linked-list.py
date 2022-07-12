# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        # put it into a stack
        stack = []
        n = head
        while n != None:
            stack.append(n)
            n = n.next
        
        # pop the stack and reverse the links
        head = stack.pop()
        prev_n = head
        while len(stack) > 0:
            n = stack.pop()
            prev_n.next = n
            prev_n = n
        n.next = None
        
        return head
