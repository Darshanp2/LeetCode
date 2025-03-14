"""
DFS - Preorder Traveral 

Time Complexity : O(N)
Space Complexity : O(N)
"""

#Recursive Approach 
def preorderTraveral(root):
    
    result = []
    def preorder(root):
        if root is None:
            return 
        result.append(root.val)
        preorder(root.left)
        preorder(root.right)

    preorder(root)
    return result

#Iterative Approach 
def preorderTraversal(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
