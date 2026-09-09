class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        counter = defaultdict(int)

        def backtrack(subset):
            if len(subset) == 2*n:
                res.append("".join(subset))
                return
            
            for brack in ['(', ')']:
                if counter['('] >= counter[')'] and counter[brack] < n:
                    subset.append(brack)
                    counter[brack] += 1
                    backtrack(subset)
                    counter[brack] -= 1
                    subset.pop()
            
        backtrack([])
        return res