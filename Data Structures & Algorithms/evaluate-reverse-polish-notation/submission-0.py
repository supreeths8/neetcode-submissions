class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        operatots = ['+', '-', '*', '/']
        for i in tokens:
            if i not in operatots:
                stack.append(int(i))
            else:
                e2 = stack.pop()
                e1 = stack.pop()
                if i == '+':
                    res = e1 + e2
                elif i == '-':
                    res = e1 - e2
                elif i == '*':
                    res = e1 * e2
                else:
                    res = int(e1 / e2)
                stack.append(res)
        return stack.pop()
