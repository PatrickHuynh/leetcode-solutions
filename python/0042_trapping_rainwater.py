class Solution:
    def trap(self, height: List[int]) -> int:
        lmbh, rmbh = 0, 0
        lhs = [0] * len(height)
        rhs = [0] * len(height)
        
        for i in range(0, len(height)):
            j = len(height)-1-i
            if height[i] > lmbh:
                lmbh = height[i]
            if height[j] > rmbh:
                rmbh = height[j]
            lhs[i] = lmbh
            rhs[j] = rmbh

        wh = 0
        for i in range(0, len(height)):
            wh += (min(lhs[i], rhs[i]) - height[i])
        
        return wh