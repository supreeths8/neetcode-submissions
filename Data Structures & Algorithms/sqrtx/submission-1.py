class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
# 13
        nearest = 0
        l,h = 1, x
        res = 1

        mid = x // 2
        while l <= h:
            mid = (l + h) // 2 # 6
            if x < mid*mid:
                h = mid - 1
            elif mid*mid < x:
                l = mid + 1
                res = mid
            else:
                return mid
        
        return res


