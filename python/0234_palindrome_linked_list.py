# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []
        current_node = head
        while (not current_node is None):
            l.append(current_node.val)
            current_node = current_node.next
        list_len = len(l)
        if list_len <= 1:
            return True
        for i in range(0,list_len):
            if l[i] != l[-1-i]:
                return False
            if (i > (list_len-1-i)):
                break
        return True