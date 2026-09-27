class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def backtrack(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + backtrack(i+2), backtrack(i+1))
            return memo[i]
        return backtrack(0)