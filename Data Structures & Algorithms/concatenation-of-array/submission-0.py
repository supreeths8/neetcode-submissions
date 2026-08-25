class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while len(ans) < 2 * len(nums):
            i = i % len(nums)
            ans.append(nums[i])
            i += 1
        return ans
        