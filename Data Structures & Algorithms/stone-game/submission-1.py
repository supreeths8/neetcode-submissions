class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            
            # Calculate who's turn and check left score
            if (r - l + 1) % 2 == 0:
                left = piles[l]
            else:
                left = 0
 
            # Check right score
            if (r - l + 1) % 2 == 0:
                right = piles[r]
            else:
                right = 0
            
            # If you take left, next has to be right and vice versa
            memo[(l,r)] = max(left + dfs(l, r - 1), right + dfs(l + 1, r))
            return memo[(l,r)]
        
        total = sum(piles)
        alice = dfs(0, len(piles) - 1)

        if alice > total - alice:
            return True
        return False