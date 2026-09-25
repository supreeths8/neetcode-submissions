class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        running_res = 0

        for op in operations:
            if op == '+':
                running_res += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                running_res += 2*stack[-1]
                stack.append(2*stack[-1])
            elif op == 'C':
                running_res -= stack[-1]
                stack.pop()
            else:
                stack.append(int(op))
                running_res += int(op)
            print(running_res)
        return running_res
            