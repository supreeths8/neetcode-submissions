class MedianFinder:

    def __init__(self):
        self._small = [] # max heap
        self._large = [] # min heap
        
    def addNum(self, num: int) -> None:
        if self._large and num > self._large[0]:
            heapq.heappush(self._large, num)
        else:
            heapq.heappush(self._small, -1 * num)
        
        if len(self._small) > len(self._large) + 1:
            val = -1 * heapq.heappop(self._small)
            heapq.heappush(self._large, val)
        if len(self._large) > len(self._small) + 1:
            val = heapq.heappop(self._large)
            heapq.heappush(self._small, -1 * val)

    def findMedian(self) -> float:
        if len(self._small) > len(self._large):
            return - 1 * self._small[0]
        elif len(self._large) > len(self._small):
            return self._large[0]
        else:
            return (-1 * self._small[0] + self._large[0]) / 2.0
        