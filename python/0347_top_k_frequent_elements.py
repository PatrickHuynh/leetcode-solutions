class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        freq = list(count.items())
        freq.sort(key=lambda x: x[1], reverse=True)
        return [i[0] for i in freq[:k]]