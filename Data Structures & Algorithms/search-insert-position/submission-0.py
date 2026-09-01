class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        res = len(nums)

        while l <= h:
            mid = (l + h) // 2
            if target <= nums[mid]:
                h = mid - 1
                res = mid
            else:
                l = mid + 1
        return res