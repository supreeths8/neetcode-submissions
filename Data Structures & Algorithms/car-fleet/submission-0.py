class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted([(pos, s) for pos,s in zip(position, speed)])[::-1]
        
        stack = []
        for p,s in pos_speed:
            remaining_dist = target - p
            remaining_time = remaining_dist / s

            stack.append(remaining_time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
            


