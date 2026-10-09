class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_converted = set(nums)
        curr_len = 0
        maxL = 0

        for num in nums:
            if num - 1 not in set_converted:
                #beginning of longestConsecutive
                cursor = num
                while cursor + curr_len in set_converted:
                    curr_len += 1
                    maxL = max(maxL, curr_len)
                curr_len = 0
        
        return maxL








        










            




        
    
        




        