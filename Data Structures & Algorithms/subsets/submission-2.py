class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        res = []
        
        def rec(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            path.append(nums[i])
            rec(i+1, path)
            path.pop()
            rec(i+1, path)
        rec(0, [])
        
        return res