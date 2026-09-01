class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        max_speed = max(piles)
        min_speed = 1

        total_hrs = 0
        res = 0

        while min_speed <= max_speed:
            mid = (min_speed + max_speed) // 2
            total_hrs = sum([math.ceil(i / mid) for i in piles])

            if total_hrs <= h:
                res = mid
                max_speed = mid - 1
            else:
                min_speed = mid + 1

        return res




        
        
            
            




        