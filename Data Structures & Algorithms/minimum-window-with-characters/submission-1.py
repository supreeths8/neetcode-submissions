class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = defaultdict(int)
        window_freq_s = defaultdict(int)
        have = 0
        minL = 100001
        R, L = 0,0

        for i in t:
            freq_t[i] += 1
        
        need = len(freq_t)
        
        l = 0

        for r in range(len(s)):
            window_freq_s[s[r]] += 1

            if s[r] in freq_t and window_freq_s[s[r]] == freq_t[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < minL:
                    minL = r - l + 1
                    L,R = l,r

                window_freq_s[s[l]] -= 1
                if s[l] in freq_t and window_freq_s[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
            
        return s[L:R+1] if minL != 100001 else ""


