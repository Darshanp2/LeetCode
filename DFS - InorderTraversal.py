"""
DFS - Inorder Traversal 

Time Complexity: O(N)
Space Complexity: O(N)
"""

#Recursive Approach 
def inorderTraversal(root):

    result = []
    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        result.append(root.val)
        inorder(root.right)
    
    inorder(root)
    return result 

#Iterative Approach
def inorderTraversal(root):

    stack = []
    result = []
    current = root 
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
    
        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result 
