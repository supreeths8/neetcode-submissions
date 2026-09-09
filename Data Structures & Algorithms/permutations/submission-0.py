class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        bool_track = [False for _ in range(len(nums))]

        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for j in range(len(bool_track)):
                if not bool_track[j]:
                    bool_track[j] = True
                    subset.append(nums[j])
                    dfs(subset)
                    subset.pop()
                    bool_track[j] = False
        
        dfs([])
        return res
