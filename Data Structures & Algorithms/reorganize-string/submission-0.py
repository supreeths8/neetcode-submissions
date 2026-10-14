class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        max_heap = [[-l, c] for c,l in freq.items()]
        heapq.heapify(max_heap)
        res = []

        prev = None

        if abs(max_heap[0][0]) > (len(s)+1) //2:
            return ""

        while max_heap:
            count, letter = heapq.heappop(max_heap)

            res.append(letter)
            count += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if count:
                prev = [count, letter]

        return "".join(res)
                    

            




