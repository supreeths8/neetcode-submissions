class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            n = min(len(prefix), len(strs[i]))
            if n == 0:
                return ""
            for j in range(n):
                if strs[i][j] != prefix[j]:
                    if j == 0:
                        return ""
                    prefix = prefix[0:j]
                    break
            prefix = prefix[0:n]

        return prefix



                

        