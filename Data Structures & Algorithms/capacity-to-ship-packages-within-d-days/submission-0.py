class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_weigh_capacity = max(weights)
        max_weight_capacity = sum(weights)

        res = max(weights)

        def isCapacitySufficient(capacity) -> bool:
            num_ships = 1
            current_capacity = capacity

            for weight in weights:
                if current_capacity - weight < 0:
                    num_ships += 1
                    current_capacity = capacity
                current_capacity -= weight
            return num_ships <= days
        
        while min_weigh_capacity <= max_weight_capacity:
            capacity = (min_weigh_capacity + max_weight_capacity) // 2
            if isCapacitySufficient(capacity):
                max_weight_capacity = capacity - 1
                res = capacity
            else:
                min_weigh_capacity = capacity + 1

        return res

            


