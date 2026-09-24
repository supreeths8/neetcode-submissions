class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = defaultdict(int)


        for l in s:
            counts[l] += 1
        
        for l in t:
            if l not in counts:
                return False
            else:
                counts[l] -= 1
        
        for _, v in counts.items():
            if v != 0:
                return False
        
        return True