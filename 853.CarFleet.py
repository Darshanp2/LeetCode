"""
853. Car Fleet 

Time Complexity: O(nlogn)

n -> visiting every node 
logn -> for sorting

"""

def carFleet(self, target, position, speed):

    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(pair)[::-1]:
        stack.append((target - position)/speed)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    
    return len(stack)