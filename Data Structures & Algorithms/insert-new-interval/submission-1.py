class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        start, end = newInterval

        # 1. intervals that end before the new one starts
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        # 2. overlapping intervals: widen the new interval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        # 3. intervals that start after the new one ends
        while i < n:
            res.append(intervals[i])
            i += 1

        return res