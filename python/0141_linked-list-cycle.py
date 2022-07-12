# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        n1 = head
        n2 = head
        while True:
            n1 = n1.next
            for i in range(2):
                n2 = n2.next    # n2 advances 2x as fast as n1
                if n2 == None:  # n2 gets to the end first (if there is an end)
                    return False
                if i == 1 and n2 == n1: # otherwise n2 will eventually come back to hit n1
                    return True