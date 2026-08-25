class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos_map = {}
        for i in range(len(nums)):
            if pos_map.get(target - nums[i]) is not None:
                if i < pos_map[target - nums[i]]:
                    return [i, pos_map[target - nums[i]]]
                else:
                    return [pos_map[target - nums[i]], i]
            pos_map[nums[i]] = i
        return []        