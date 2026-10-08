class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_freq = defaultdict(int)
        maxFreq = 0
        l = 0
        maxL = 0

        for r in range(len(s)):
            window_freq[s[r]] += 1
            maxFreq = max(maxFreq, window_freq[s[r]])

            while r - l + 1 - maxFreq > k:
                window_freq[s[l]] -= 1
                l += 1
            maxL = max(maxL, r - l + 1)
        
        return maxL


