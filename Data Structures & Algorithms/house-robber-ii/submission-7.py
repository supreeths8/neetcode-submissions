class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def backtack(i, nums_, first_taken):
            if i >= len(nums_):
                return 0
            if (i,first_taken) in memo:
                return memo[(i,first_taken)]
            
            memo[(i, first_taken)] = max(nums_[i] + backtack(i+2, nums_, first_taken), backtack(i+1, nums_, first_taken))
            return memo[(i, first_taken)]
        return max(backtack(0, nums[1:], False), backtack(0, nums[:-1], True))
            