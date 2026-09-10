class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        bool_state = [False for _ in range(len(nums))]

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if bool_state[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not bool_state[i - 1]:
                    continue

                bool_state[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                bool_state[i] = False
            
        backtrack([])
        return res