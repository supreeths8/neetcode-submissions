class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2":"abc",
        "3":"def", "4":"ghi", "5":"jkl", "6":"mno",
        "7":"pqrs", "8":"tuv", "9":"wxyz"}

        res = []

        def backtrack(i, subset):
            if digits == "":
                return
            
            if i == len(digits):
                res.append("".join(subset))
                return
            
            letters = mapping[digits[i]]
            for l in letters:
                subset.append(l)
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return res



