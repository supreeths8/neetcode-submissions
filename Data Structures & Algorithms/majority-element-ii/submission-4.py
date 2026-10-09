class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        print(nums)

        l = 0
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                count = r - l
                if count > len(nums) / 3:
                    res.append(nums[l])
                l = r
                count = 0
        
        if len(nums) - l > len(nums) / 3:
            res.append(nums[l])

        return res