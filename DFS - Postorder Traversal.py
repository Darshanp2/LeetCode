"""
DFS - Postorder Traversal 

Time Complexity: O(N)
Space Complexity: O(N)
"""

#Recursive Approach 
def postorderTraversal(root):

    result = []
    def postorder(root):
        if not root:
            return 
        postorder(root.left)
        postorder(root.right)
        result.append(root.val)
    
    postorder(root)
    return result

#Iterative Approach 
def postorderTraversal(root):

    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    return result

