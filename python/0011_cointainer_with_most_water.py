class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_area = 0
        prev_min_height = 0
        while i < j:
            min_height = min(height[i], height[j])
            max_area = max(max_area, (j-i) * min_height)
            if height[i] < height[j]:
                while height[i] <= min_height and i < j:
                    i += 1
            else:
                while height[j] <= min_height and i < j:
                    j -= 1
        return max_area