class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset=[], c_sum=0):
            if c_sum == target:
                res.append(subset[:])
                return
            
            # c_sum += nums[i]
            # subset.append(nums[i])
            # dfs(i, subset, c_sum)
            # c_sum -= nums[i]
            # subset.pop()
            # dfs(i+1, subset, c_sum)

            for j in range(i, len(nums)):
                if c_sum + nums[j] > target:
                    return
                c_sum += nums[j]
                subset.append(nums[j])
                dfs(j, subset, c_sum)
                c_sum -= nums[j]
                subset.pop()

        dfs(0)
        return res


