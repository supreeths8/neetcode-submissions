class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prods = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_prods[i] = prefix_prods[i - 1] * nums[i - 1]

        running_prod = nums[len(nums) - 1]
        res[len(nums) - 1] = prefix_prods[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] = prefix_prods[i] * running_prod
            running_prod *= nums[i]

        return res
