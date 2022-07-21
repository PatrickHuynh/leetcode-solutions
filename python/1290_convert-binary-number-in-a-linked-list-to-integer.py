# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        n = head
        while n is not None:
            nums.append(n.val)
            n = n.next
        num = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                num += 2 ** (nums[i] * (len(nums) + ~i))
        return num