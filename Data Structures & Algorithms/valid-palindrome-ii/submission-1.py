class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palidrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                
                r -= 1
                l += 1
            return True
        

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                res = is_palidrome(l + 1, r) or is_palidrome(l, r - 1)
                return res
            r -= 1
            l += 1
        return True