"""
101. Symmetric Tree

Time Complexity :O(N)
Space Complexity : O(H)

"""
#Using Recursive Approach 

def symmetric(self, root: Optional[TreeNode]) -> bool:

    def dfs(left, right):

        if not left and not right:
            return True
        if not left or not right:
            return False
    
        return(left.val == right.val and 
               dfs(left.left, right.right) and 
               dfs(left.right, right.left)
        )
        
    return dfs(root.left, root.right)

#Using Iterative Approach 
from collections import deque

def symmetric(self, root: Optional[TreeNode]) -> bool:
    
    if not root:
        return True

    queue = deque([(root.left, root.right)])

    while queue:
        left, right = queue.popleft()

        if not left and not right:
            continue

        if not left or not right or left.val != right.val:
            return False
    
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True

