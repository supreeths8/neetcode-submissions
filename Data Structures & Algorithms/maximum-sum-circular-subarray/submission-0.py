class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        minSum = nums[0]
        maxSum = nums[0]
        currMin = float('inf')
        currMax = float('-inf')

        for n in nums:
            total_sum += n

            currMax = max(currMax + n, n)
            maxSum = max(maxSum, currMax)

            currMin = min(currMin + n, n)
            minSum = min(minSum, currMin)

        if maxSum < 0:
            return int(maxSum)

        return int(max(maxSum, total_sum - minSum))