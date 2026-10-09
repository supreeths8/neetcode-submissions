class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        freq_to_num = defaultdict(list)
        res = []

        for n in nums:
            freq_map[n] += 1
        
        for n,freq in freq_map.items():
            freq_to_num[freq].append(n)

        for freq in range(len(nums), 0,-1):
            freq_nums = freq_to_num[freq]
            for n in freq_nums:
                if len(res) < k:
                    res.append(n)
        
        return res