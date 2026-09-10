class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag_up = set()
        diag_down = set()

        res = 0

        def backtrack(row):
            nonlocal res

            if row == n:
                res += 1
                return
            
            for col in range(n):
                if col in cols or (row  - col) in diag_down or (row + col) in diag_up:
                    continue
                
                cols.add(col)
                diag_down.add(row - col)
                diag_up.add(row + col)
                backtrack(row + 1)
                cols.remove(col)
                diag_down.remove(row - col)
                diag_up.remove(row + col)

        backtrack(0)
        return res
            