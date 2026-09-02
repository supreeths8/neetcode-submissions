class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1 for _ in range(len(nums))]
        suffixes = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1,-1):
            suffixes[i] = suffixes[i + 1] * nums[i + 1]

        res = []
        for i in range(len(nums)):
            res.append(prefixes[i] * suffixes[i])
        
        return res



        
        