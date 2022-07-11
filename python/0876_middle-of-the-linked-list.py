# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        listlen = 0
        n = head
        while n != None:
            listlen += 1
            output.append(n)
            n = n.next
        return output[listlen//2]