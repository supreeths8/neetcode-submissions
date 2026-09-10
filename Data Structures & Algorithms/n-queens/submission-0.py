class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        diag_down = set()
        diag_up = set()
        cols = set()

        def backtrack(row):
            if row == n:
                res.append(["".join(rr) for rr in board.copy()])
                return
            

            for col in range(n):
                if col in cols or (row + col) in diag_up or (row - col) in diag_down:
                    continue
                
                cols.add(col)
                diag_up.add(row + col)
                diag_down.add(row - col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                diag_up.remove(row + col)
                diag_down.remove(row - col)
                board[row][col] = "."
        backtrack(0)
        return res


