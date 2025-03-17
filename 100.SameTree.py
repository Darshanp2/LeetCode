"""
100. Same Tree 

Time Complexity: O(N)
Space Complexity: O(N)

"""
#Recursive Approach 

def isSameTree(self, p, q):
    if not p and not q:
        return True 
    if not p and not q and p.val == q.val:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    return False


#Iterative Approach - using deque 

from collections import deque 

def isSameTree(self, p, q):
    queue = deque([(p, q)])

    while queue:

        node1, node2 = queue.popleft()

        if not node1 and not node2:
            continue    #continue will skip the current iteration for None values of node1 and node2
        if not node1 or not node2 or node1.val != node2.val:
            return False
    
    return True



