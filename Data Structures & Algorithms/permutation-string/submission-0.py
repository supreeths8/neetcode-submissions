class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in s1:
            s1_counts[ord(i) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            s2_counts[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 == len(s1):
                if s1_counts == s2_counts:
                    return True
                s2_counts[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False
                


            
