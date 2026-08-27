class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        i,j = 0,0
        res = []

        nums.sort()

        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j - i > len(nums) // 3:
                res.append(nums[i])
            i = j
        
        return res



        

        