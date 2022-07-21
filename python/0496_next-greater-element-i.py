class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        for idx, i in enumerate(nums1):
            count = False
            for j in nums2:
                if not count and i == j:
                    count = True
                if count and j > i:
                    result[idx] = j
                    break
        return result