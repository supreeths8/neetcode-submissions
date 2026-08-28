class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        longest = 0
        length = 0

        for n in nums:
            if n - 1 not in nums:
                length = 1
                while n + length in nums:
                    length += 1
            longest = max(longest, length)
        return longest




            




        
    
        




        