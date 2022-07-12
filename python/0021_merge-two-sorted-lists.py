# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
            
        curr_node = head
        while True:
            if list1 == None:
                curr_node.next = list2
                break

            if list2 == None:
                curr_node.next = list1
                break
        
            if list1.val <= list2.val:
                curr_node.next = list1
                curr_node = curr_node.next
                list1 = list1.next
            else:
                curr_node.next = list2
                curr_node = curr_node.next
                list2 = list2.next
                
        return head
        
        
        
        
        