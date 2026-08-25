class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for num in nums:
            if count_map.get(num):
                return True
            count_map[num] = 1
        return False
        