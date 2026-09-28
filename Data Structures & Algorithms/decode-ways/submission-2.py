class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def backtrack(i):
            if i == len(s):
                return 1
            # '0' on its own maps to nothing so return a 0. 
            # Then skip the 
            if s[i] == '0':
                return 0
            
            if i in memo:
                return memo[i]
            
            res = backtrack(i+1)
            
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                res += backtrack(i+2)
            memo[i] = res
            return res
        return backtrack(0)

 