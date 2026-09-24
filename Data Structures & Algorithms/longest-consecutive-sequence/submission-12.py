class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Use sets.
        Identify the start of the sequence. Then check if the 
        consecutive element exists or not. Increase the counter.
        The hint also says O(n) which validates hashset approach.
        Cannot use sliding window as there is no monotonicity
        """
        if len(nums) == 0:
            return 0
        
        nums_set = set(nums)
        length = 0
        maxL = 0

        for n in nums:
            if n - 1 not in nums_set:
                length = 1
                while n + length in nums_set:
                    length += 1
                maxL = max(maxL, length)

        return maxL






        










            




        
    
        




        