class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = min(len(s1), len(s2))
        s1_map = [0] * 26
        s2_map = [0] * 26
        l = 0

        if len(s2) < len(s1):
            return False
        
        for s in s1:
            s1_map[ord(s) - ord('a')] += 1

        for r in range(len(s2)):
            s2_map[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 == len(s1):
                if s1_map == s2_map:
                    return True
                
                s2_map[ord(s2[l]) - ord('a')] -= 1
                l += 1
        
        return False

