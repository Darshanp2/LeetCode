"""
112. Path Sum 

DFS Recursive Approach 

Time Complexity : O(N)
Space Complexity : O(H), where H is the height of the tree0

"""
def __init__(self, val=0, left=None, right=None):
    self.val = val 
    self.left = left
    self.right = right 

def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

    def dfs(node, curSum):

        if not node:
            return False 
    
        curSum += node.val

        if not node.left and not node.right:
            return curSum == targetSum
    
        return (dfs(node.left, curSum) or dfs(node.right, curSum))

    return dfs(root, 0)