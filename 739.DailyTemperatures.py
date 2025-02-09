"""
739. Daily Temperatures

Logic: Using Stack 

Time Complexity : O(n)
Space Complexity : O(n)

"""
def dailyTemperatures(self, temperatures):

    res = [0] * len(temperatures)
    stack = [] #storing in pairs [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            res[stackIndex] = (i - stackIndex)
        
        stack.append([t, i])
    
    return res