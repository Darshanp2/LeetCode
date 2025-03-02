"""
543. Diameter of Binary Tree

Time Complexity: O(N)
Space Complexity: O(h)

"""

def diameterofBinaryTree(self, root: Optional[TreeNode]) -> int:
    res = 0 

    def dfs(curr):
        if not curr:
            return 0 
        
        left = dfs(curr.left)
        right = dfs(curr.right)

        nonlocal res
        res = max(res, left + right)        #Calculating Diameter
        return 1 + max(left, right)         #Calculating Height

    dfs(root)
    return res 