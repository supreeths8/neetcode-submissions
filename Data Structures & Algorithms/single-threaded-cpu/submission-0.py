class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort()
        
        min_heap = []
        time = tasks[0][0]
        i = 0
        res = []

        while i < len(tasks) or min_heap:
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, [tasks[i][1], tasks[i][2]])
                i += 1

            if min_heap:
                pTime, idx = heapq.heappop(min_heap)
                time += pTime
                res.append(idx)
            else:
                time = tasks[i][0]

        return res