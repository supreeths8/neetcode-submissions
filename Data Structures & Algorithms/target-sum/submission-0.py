class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(i, currTarget):
            if i == len(nums):
                if currTarget == 0:
                    return 1
                return 0
            if (i, currTarget) in cache:
                return cache[(i, currTarget)]

            res = dfs(i+1, currTarget - nums[i])
            res2 = dfs(i + 1, currTarget + nums[i])

            cache[(i, currTarget)] = res + res2
            return cache[(i, currTarget)]

        return dfs(0, target)