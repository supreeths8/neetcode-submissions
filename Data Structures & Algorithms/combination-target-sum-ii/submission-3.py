class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, currSum, path):

            if currSum == target:
                res.append(path[:])
                return
            if currSum > target or i >= len(candidates):
                return
            

            currSum += candidates[i]
            path.append(candidates[i])
            dfs(i+1, currSum, path)
            path.pop()
            currSum -= candidates[i]

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, currSum, path)
        
        dfs(0, 0, [])
        return res

            

                         