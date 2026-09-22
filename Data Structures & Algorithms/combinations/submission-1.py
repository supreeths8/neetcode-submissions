class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if len(path) == k:
                res.append(path[:])
                return
            if i > n:
                return
            
            path.append(i)
            dfs(i+1, path)
            path.pop()

            dfs(i+1, path)

        dfs(1, [])
        return res