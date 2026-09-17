class MinStack:

    def __init__(self):
        self._stack = []
        self._prefix = []
        

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._prefix:
            self._prefix.append(val)
        else:
            self._prefix.append(min(val, self._prefix[-1]))


    def pop(self) -> None:
        el = self._stack.pop()
        self._prefix.pop()
        
    def top(self) -> int:
        return self._stack[-1]
        

    def getMin(self) -> int:
        return self._prefix[-1]
    