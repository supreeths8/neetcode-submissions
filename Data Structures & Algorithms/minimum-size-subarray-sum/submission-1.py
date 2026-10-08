class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = float("inf")
        running_sum = 0

        l = 0

        for r in range(len(nums)):
            running_sum += nums[r]

            while running_sum >= target:
                minL = min(minL, r - l + 1)
                running_sum -= nums[l]
                l += 1

        return 0 if minL == float('inf') else int(minL)
