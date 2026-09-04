class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freqs = [[] for _ in range(0, len(nums) + 1)]

        for n in nums:
            counts[n] += 1
        
        for n, c in counts.items():
            freqs[c].append(n)
        
        res = []

        for i in range(len(freqs) - 1, 0, -1):
            for j in freqs[i]:
                res.append(j)
            if len(res) == k:
                return res
        
        return res
