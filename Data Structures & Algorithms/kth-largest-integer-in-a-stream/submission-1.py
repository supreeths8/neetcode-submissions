class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums = [-n for n in nums]
        heapq.heapify(nums)
        self.max_heap = nums
        

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        i = self.k
        collect = []
        val = -1
        while i:
            val = heapq.heappop(self.max_heap)
            collect.append(val)
            i -= 1
        
        for c in collect:
            heapq.heappush(self.max_heap, c)
        
        return -val

