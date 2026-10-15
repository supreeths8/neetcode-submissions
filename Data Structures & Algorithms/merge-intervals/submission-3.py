class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for i in range(len(intervals)):
            if res and res[-1][1] >= intervals[i][0]:
                res[-1] = [min(intervals[i][0], res[-1][0]),max(intervals[i][1], res[-1][1])]
            else:
                res.append(intervals[i])

        return res
