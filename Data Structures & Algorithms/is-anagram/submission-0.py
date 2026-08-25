class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapp = {}
        for c in s:
            mapp[c] = mapp.get(c, 0) + 1
        for c in t:
            mapp[c] = mapp.get(c, 0) - 1
        print(mapp)
        
        for i in mapp.values():
            if i != 0:
                return False
        return True




        