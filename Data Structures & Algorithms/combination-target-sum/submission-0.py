class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i=0, subset=[], c_sum=0):
            if i >= len(nums) or c_sum > target:
                return
            
            if c_sum == target:
                res.append(subset[:])
                return
            
            c_sum += nums[i]
            subset.append(nums[i])
            dfs(i, subset, c_sum)
            c_sum -= nums[i]
            subset.pop()
            dfs(i+1, subset, c_sum)
        dfs()
        return res


