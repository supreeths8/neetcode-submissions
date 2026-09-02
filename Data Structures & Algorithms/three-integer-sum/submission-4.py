class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            # Avoid repetition in the 1st num selection.
            # If this repeates, the while loop will give the same 
            # two other numbers -> full list repeats.
            if i > 0 and num == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if num + nums[l] + nums[r] < 0:
                    l += 1
                elif num + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    # This advances the pointer after one result
                    l += 1
                    # Once we append result, we cannot repeat it.
                    # If nums[l] is same, then nums[r] will also
                    # be the same. So, do not allow repeats here
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res




        