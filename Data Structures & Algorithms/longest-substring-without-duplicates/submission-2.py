class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        leng = 0
        check_set = set()
        for r in range(len(s)):
            while s[r] in check_set:
                check_set.remove(s[l])
                l += 1
            check_set.add(s[r])
            leng = max(leng, r - l + 1)
        return leng


        