class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        freq_collection = defaultdict(list)
        res = []

        for n in nums:
            freq_map[n] += 1
        

        for n, freq in freq_map.items():
            freq_collection[freq].append(n)

        for freq in range(len(nums), 0, -1):
            for element in freq_collection[freq]:
                res.append(element)
                if len(res) == k:
                    return res
        
        return res

