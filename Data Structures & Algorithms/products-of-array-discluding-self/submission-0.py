class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1 for _ in range(len(nums))]
        sufixes = [1 for _ in range(len(nums))]

        prod = []

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            sufixes[j] = sufixes[j + 1] * nums[j + 1]

        for i in range(len(nums)):
            prod.append(prefixes[i] * sufixes[i])
        return prod


        
        