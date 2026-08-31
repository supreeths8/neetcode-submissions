class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        freq_window = defaultdict(int)
        freq_t = defaultdict(int)
        for k in t:
            freq_t[k] += 1
        
        have, need = 0, len(freq_t)
        idx = [-1,-1]

        min_l = float('inf')

        while r < len(s):
            freq_window[s[r]] += 1

            if s[r] in freq_t and freq_window[s[r]] == freq_t[s[r]]:
                have += 1
            
            while need == have:
                if r - l + 1 < min_l:
                    min_l = r - l + 1
                    idx = [l, r]
                
                freq_window[s[l]] -= 1
                if s[l] in freq_t and freq_window[s[l]] < freq_t[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return s[idx[0]: idx[1] + 1] if min_l is not float('inf') else ""



