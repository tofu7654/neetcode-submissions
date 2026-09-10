class MinStack:

    def __init__(self):
        self.stack, self.minStack = [], []

    def push(self, val: int) -> None:
        # add the new value to the stack
        self.stack.append(val)
        # compare the new value with the current min
        val = min(val, self.minStack[-1] if self.minStack else val)
        # append the new min to the minstack
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # always called with non empty stack
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
