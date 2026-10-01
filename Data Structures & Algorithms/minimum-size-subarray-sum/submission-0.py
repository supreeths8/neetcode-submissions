class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0

        minL = float('inf')
        runningSum = 0
        while r < len(nums):
            runningSum += nums[r]
            while runningSum >= target:
                minL = min(r - l + 1, minL)
                runningSum -= nums[l]
                l += 1
            r += 1
        return 0 if minL == float('inf') else int(minL)

