"""
232. Implement Queue using Stacks

Simple Approach

Time Complexity:
Push operation - O(1) 
Pop and Peek operation - (O)n 

"""

class MyQueue(object):

    def __init__(self):
        self.stack1, self.stack2 = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())

        ret_pop_val = self.stack2.pop()
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        return ret_pop_val

    def peek(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        
        ret_val = self.stack2.pop()
        self.stack2.append(ret_val)

        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        return ret_val
        
    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack1) == 0:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()