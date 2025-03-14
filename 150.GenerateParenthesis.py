"""
22. Generate Parenthesis

Time Complexity: O(n)
Space Complexity: O(n)

Using Stack

"""

def generateParenthesis(self, n):

    stack = []
    res = []

    def backtrack(openN, closeN):

        if openN == closeN == n:
            res.append("".join(stack))
            return 
    
        if openN < n:
            stack.append('(')
            backtrack(openN+1, closeN)
            stack.pop()
        
        if closeN < openN:
            stack.append(')')
            backtrack(openN, closeN+1)
            stack.pop()

    backtrack(0, 0)
    return res 