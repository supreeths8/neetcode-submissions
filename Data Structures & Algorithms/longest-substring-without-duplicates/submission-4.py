class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        leng = 0
        pos_set = set()

        for r in range(len(s)):
            while s[r] in pos_set:
                pos_set.remove(s[l])
                l += 1
            pos_set.add(s[r])
            leng = max(r - l + 1, leng)

        return leng

        