class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        max_freq = 0
        max_len = 0
        freq_pos = defaultdict(int)

        for r in range(len(s)):
            freq_pos[s[r]] += 1

            max_freq = max(max_freq, freq_pos[s[r]])
            if (r - l + 1) - max_freq <= k:
                max_len = max(max_len, r - l + 1)
            else:
                freq_pos[s[l]] -= 1
                l += 1
        return max_len


