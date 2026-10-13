class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            diff = -first - (-second)
            if diff == 0:
                pass
            else:
                heapq.heappush(max_heap, -diff)
        
        return -max_heap[0] if max_heap else 0
