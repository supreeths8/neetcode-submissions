class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        nums.sort()
        print(nums)
        curr = nums[0]
        streak = 0
        max_streak = 0

        for i in range(1, len(nums)):
            if curr == nums[i]:
                continue
            curr += 1
            if curr == nums[i]:
                streak += 1
            else:
                curr = nums[i]
                streak = 0
            max_streak = max(streak, max_streak)
        return max_streak + 1

            




        
    
        




        