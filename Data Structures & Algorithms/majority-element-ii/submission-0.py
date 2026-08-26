class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_map = {}
        threshold = len(nums) // 3
        res = set()
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1
            if count_map[n] > threshold:
                res.add(n)
        return list(res)

        