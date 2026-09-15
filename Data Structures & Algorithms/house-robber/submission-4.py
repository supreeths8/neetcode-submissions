class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * (len(nums) + 1)

        def backtrack(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(nums[i] + backtrack(i+2), backtrack(i+1)) 
            return memo[i]

        res = backtrack(0)
        return res
