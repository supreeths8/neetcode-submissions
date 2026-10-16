class MedianFinder:

    def __init__(self):
        self._first_half = [] # max heap
        self._second_half = [] # min heap
        
    def addNum(self, num: int) -> None:
        if self._second_half and self._second_half[0] > num:
            heapq.heappush(self._first_half, -num)
        else:
            heapq.heappush(self._second_half, num)

        if len(self._second_half) > len(self._first_half) + 1:
            val = heapq.heappop(self._second_half)
            heapq.heappush(self._first_half, -val)
        if len(self._first_half) > len(self._second_half) + 1:
            val = heapq.heappop(self._first_half)
            heapq.heappush(self._second_half, -val)

    def findMedian(self) -> float:
        if len(self._first_half) > len(self._second_half):
            return -self._first_half[0]
        elif len(self._second_half) > len(self._first_half):
            return self._second_half[0]
        return (-self._first_half[0] + self._second_half[0]) / 2
        
        