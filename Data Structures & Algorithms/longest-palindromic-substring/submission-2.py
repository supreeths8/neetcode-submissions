class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = 0
        maxR = 0
        maxLen = 0


        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxL = l
                    maxR = r
                r += 1
                l -= 1
        
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxL = l
                    maxR = r
                r += 1
                l -= 1
        
        return s[maxL:maxR+1]

