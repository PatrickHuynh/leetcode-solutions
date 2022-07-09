class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            num_dict[str(num)] = num_dict.get(str(num),0) + 1
            if num_dict[str(num)] > 1:
                return True
        return False