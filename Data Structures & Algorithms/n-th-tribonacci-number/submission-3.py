class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def backtrack(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if i in memo:
                return memo[i]

            memo[i] = backtrack(i - 3) + backtrack(i-2) + backtrack(i-1)
            return memo[i]
        return backtrack(n)