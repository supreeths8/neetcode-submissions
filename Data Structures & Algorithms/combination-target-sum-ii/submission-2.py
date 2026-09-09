class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, subset, c_sum):

            if c_sum == target:
                res.append(subset[:])
                return
            if i >= len(candidates):
                return
                        
            for j in range(i, len(candidates)):
                if c_sum + candidates[j] > target:
                    return
                
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                c_sum += candidates[j]
                subset.append(candidates[j])
                dfs(j + 1, subset, c_sum)
                subset.pop()
                c_sum -= candidates[j]
        
        dfs(0, [], 0)
        return res

