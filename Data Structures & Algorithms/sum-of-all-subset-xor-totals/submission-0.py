class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0

        def backtrack(i, subsets):
            nonlocal res
            if i == len(nums):
                k = 0
                for n in subsets:
                    k = k ^ n
                res += k
                return
            
            subsets.append(nums[i])
            backtrack(i+1, subsets)
            subsets.pop()
            backtrack(i+1, subsets)
        
        backtrack(0, [])
        return res
