class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = float('-inf')

        for n in nums:
            currSum = max(currSum + n, n)
            maxSum = max(maxSum, currSum)
        
        return int(maxSum)

