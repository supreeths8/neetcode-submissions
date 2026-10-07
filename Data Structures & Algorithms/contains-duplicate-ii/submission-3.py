class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_in_window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                seen_in_window.remove(nums[l])
                l += 1
            
            if nums[r] in seen_in_window:
                return True
            
            seen_in_window.add(nums[r])
        
        return False