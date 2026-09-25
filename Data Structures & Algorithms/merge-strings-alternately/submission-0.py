class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        r1, r2 = 0,0

        while r1 < len(word1) and r2 < len(word2):
            res.append(word1[r1])
            res.append(word2[r2])

            r1 += 1
            r2 += 1

        while r1 < len(word1):
            res.append(word1[r1])

            r1 += 1
        
        while r2 < len(word2):
            res.append(word2[r2])
            r2 += 1
        
        return "".join(res)
