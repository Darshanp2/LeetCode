from collections import deque 

def bfsTraversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        
    return result
