class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        l = 0
        r = 1
        n = len(nums)
        res = []

        while r < len(nums):
            if nums[l] == nums[r]:
                pass
            else:
                running_len = r - l
                if running_len > n // 3:
                    res.append(nums[l])
                l = r
                
            r += 1
        # When r reaches end of loop
        running_len = len(nums) - l
        if running_len > n // 3:
            res.append(nums[l])
        return res





        

        