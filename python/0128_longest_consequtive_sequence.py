class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = 0
        max_count = 0
        nums = list(set(nums))
        nums.sort()

        checknum = nums[0]
        for num in nums:
            if checknum == num:
                count += 1
                checknum += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1
                checknum = num + 1
        if count > max_count:
            max_count = count

        return max_count