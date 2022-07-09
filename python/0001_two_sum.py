class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ndict = {}
        for idx, num in enumerate(nums):
            sol = target - num
            if sol in ndict.keys():
                return [ndict[sol], idx]
            else:
                ndict[num] = idx
        return None