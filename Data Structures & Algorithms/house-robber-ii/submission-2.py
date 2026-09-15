class Solution:
    def rob(self, nums: List[int]) -> int:
        # if len(nums) < 3:
        #     return max(nums)

        # nums1 = nums[:-1]
        # nums2 = nums[1::]
        
        # def backtrack(_nums, i):
        #     if i >= len(_nums):
        #         return 0
            
        #     return max(_nums[i] + backtrack(_nums, i+2), backtrack(_nums, i+1))

        # return max(backtrack(nums1, 0), backtrack(nums2, 0))
        memo = [[-1,-1] for _ in range(len(nums))] 

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            if memo[i][flag] != -1:
                return memo[i][flag]

            memo[i][flag] = max(nums[i] + dfs(i+2, flag or i == 0), dfs(i+1, flag))
            return memo[i][flag]
        return max(dfs(0, False), dfs(0, True))