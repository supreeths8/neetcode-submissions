# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        h = n - 1

        while l <= h:
            mid = (l + h) // 2
            guess_result = guess(mid)
            if guess_result == -1:
                h = mid - 1
            elif guess_result == 1:
                l = mid + 1
            else:
                return mid
        return n

