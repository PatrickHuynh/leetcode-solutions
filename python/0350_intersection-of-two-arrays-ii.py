class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = {}
        res = []
        for n in nums1:
            d1[n] = d1.get(n, 0) + 1
        for n in nums2:
            v1 = d1.get(n,0)
            if v1 > 0:
                res.append(n)
                d1[n] -= 1
        return res