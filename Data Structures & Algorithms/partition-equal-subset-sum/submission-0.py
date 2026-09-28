class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        cache = {}
        
        def dfs(i, target):
            if i == len(nums):
                if target == 0:
                    return True
                return False
            if (i, target) in cache:
                return cache[(i, target)]
            
            res = dfs(i+1, target) or dfs(i+1, target - nums[i])
            cache[(i, target)] = res
            return res
        
        return dfs(0, sum(nums) // 2)
