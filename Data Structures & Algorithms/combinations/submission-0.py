class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, 1 + n)]

        res = []

        def backtrack(i, combos):
            if len(combos) == k:
                res.append(combos[:])
                return
            if i >= len(nums):
                return
            
            combos.append(nums[i])
            backtrack(i+1, combos)
            combos.pop()

            backtrack(i + 1, combos)
        
        backtrack(0,[])
        return res