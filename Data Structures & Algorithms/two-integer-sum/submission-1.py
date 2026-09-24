class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i in range(len(nums)):
            if target - nums[i] in mapp:
                if i > mapp[target - nums[i]]:
                    return [mapp[target - nums[i]], i]
                else:
                    return [i, mapp[target - nums[i]]]

            mapp[nums[i]] = i
        