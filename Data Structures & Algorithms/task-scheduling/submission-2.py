class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-c for c in counts.values()]
        heapq.heapify(max_heap)
        cooldown_q = deque()

        t = 0

        while max_heap or cooldown_q:
            t += 1
            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count:
                    cooldown_q.append((count, t + n))

            if cooldown_q and cooldown_q[0][1] == t:
                count = cooldown_q.popleft()[0]
                heapq.heappush(max_heap, count)

        return t

