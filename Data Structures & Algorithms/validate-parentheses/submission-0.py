class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                last = stack.pop()

                if not(last == '(' and char == ')' or last == '[' and char == ']' or last == '{' and char == '}'):
                    return False
        
        return not stack

        