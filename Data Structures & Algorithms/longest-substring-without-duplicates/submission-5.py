class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        maxL = 0
        seen_in_window = set()

        for r in range(len(s)):
            while s[r] in seen_in_window:
                seen_in_window.remove(s[l])
                l += 1

            maxL = max(maxL, r - l + 1)
            seen_in_window.add(s[r])
        
        return maxL

