class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        memo = {}

        def backtrack(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            res = backtrack(i+1)
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] < '7')):
                memo[i+2] = backtrack(i+2)
                res += memo[i+2]

            memo[i] = res
            return res
        return backtrack(0)
