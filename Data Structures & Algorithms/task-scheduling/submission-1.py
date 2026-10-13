class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        queue = deque()

        t = 0
        max_heap = [-f for f in frequencies.values()]
        heapq.heapify(max_heap)

        while max_heap or queue:
            t += 1

            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                if cnt:
                    queue.append((cnt, t + n))

            if queue and queue[0][1] == t:
                task = queue.popleft()[0]
                heapq.heappush(max_heap, task)
        
        return t
