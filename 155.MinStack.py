"""
155. Min Stack

Time Complexity: O(n)

"""

def minStack(self, val):
    """
    type val: int
    rtype: None"
    """

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
    
    def minStack(self):
        return self.minStack[-1]