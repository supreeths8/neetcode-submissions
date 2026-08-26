class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for i in nums:
            counts[i] += 1
        
        index = 0
        for i in range(3):
            while counts[i]:
                counts[i] -= 1
                nums[index] = i
                index += 1

        
        