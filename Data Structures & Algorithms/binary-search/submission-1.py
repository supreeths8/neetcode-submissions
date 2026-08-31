class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        def recc(l, h):
            if l > h:
                return - 1
            mid = (l + h) // 2
            if target < nums[mid]:
                return recc(l, mid - 1)
            elif nums[mid] < target:
                return recc(mid + 1, h)
            else:
                return mid
        
        res = recc(low, high)
        return res


        # while low <= high:
        #     mid = (low + high) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        # return -1

