class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)
        cooldown_q = deque()

        t = 0

        while max_heap or cooldown_q:
            t += 1

            if max_heap:
                c = 1 + heapq.heappop(max_heap)
                if c:
                    cooldown_q.append((c, t + n))

            if cooldown_q and t == cooldown_q[0][1]:
                heapq.heappush(max_heap, cooldown_q.popleft()[0])

        return t

