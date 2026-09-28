class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = [[-1] * (capacity+1) for _ in range(len(profit) + 1)]
        print(cache)

        def backtrack(i, currentCapacity):
            if i == len(profit):
                return 0

            if cache[i][currentCapacity] != -1:
                return cache[i][currentCapacity]
            
            maxProfit = backtrack(i+1, currentCapacity)

            newCapacity = currentCapacity - weight[i]
            if newCapacity >= 0:
               P = profit[i] + backtrack(i+1, newCapacity)
               maxProfit = max(maxProfit, P)
            cache[i][currentCapacity] = maxProfit

            return cache[i][currentCapacity]

        return backtrack(0, capacity)