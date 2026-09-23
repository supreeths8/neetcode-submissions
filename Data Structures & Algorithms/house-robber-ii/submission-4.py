class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        

        def robC(nums_):
            if not nums_:
                return 0
            if len(nums_) == 1:
                return nums_[0]

            n = len(nums_)
            dp = [0] * n

            dp[0] = nums_[0]
            dp[1] = max(nums_[0], nums_[1])

            for i in range(2, n):
                dp[i] = max(dp[i-2] + nums_[i], dp[i - 1])
            return dp[n-1]
        
        res = max(robC(nums[:-1]), robC(nums[1:]))
        return res

