class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1,1

        for n in nums:
            t = currMax * n
            currMax = max(currMax * n, n * currMin, n)
            currMin = min(t, currMin * n, n)
            res = max(currMax, res)
        
        return res
                
