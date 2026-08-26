class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2

        freq_map = {}
        max_count = 0
        res = 0

        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
            max_count = max(max_count, freq_map[n])
            if max_count > threshold:
                return n
    

        