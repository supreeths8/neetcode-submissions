class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currSum, path):
            if currSum > target:
                return
            if currSum == target:
                res.append(path[:])
                return res
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                currSum += nums[j]

                dfs(j, currSum, path)
                currSum -= nums[j]
                path.pop()
        dfs(0,0,[])
        return res