"""
102. Binary Tree Level Order Traversal 

Time Complexity: O(N)
Space Compleixty: O(N)
"""
from Collection import deque 

class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
    if not root:  
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
        
            if node.right:
                queue.append(node.right)

        result.append([level])

    return result 