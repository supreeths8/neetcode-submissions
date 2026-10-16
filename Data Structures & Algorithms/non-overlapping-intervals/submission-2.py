class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prev_end = intervals[0][1]

        for interval in intervals[1:]:
            if prev_end > interval[0]:
                res += 1
                prev_end = min(prev_end, interval[1])
            else:
                prev_end = interval[1]

        return res
