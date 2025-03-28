"""
993. Cousins in Binary Tree

Time Complexity: O(N)
Space Complexity: O(H)

"""
def isCousins(self, root: Optional[TreeNode], x:int, y:int) -> bool:

    tracker = {}

    def dfs(node, parent, depth, x, y):

        if not node:
            return 
    
        dfs(node.left, node, depth+1, x, y)
        dfs(node.right, node, depth+1, x, y)

        if node.val in (x,y):
            tracker[node.val] = (parent, depth)
        
    dfs(root, None, 0, x, y)

    cousins = tracker.get(x) and tracker.get(y) and tracker[x][0] != tracker[y][0] and tracker[x][1] == tracker[y][1]

    return cousins