class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temp:
                prev_temp = stack.pop()
                ans[prev_temp[0]] = idx - prev_temp[0]
            stack.append((idx, temp))
        return ans