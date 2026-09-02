class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        res = -1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pivot = l
        
        def bs(l,r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        res = bs(0, pivot - 1)
        if res == -1:
            return bs(pivot, len(nums) - 1)
        return res
        


        