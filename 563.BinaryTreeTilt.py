"""

563. Binary Tree Tilt

Time Complexity: O(n)
Space Complexity: O(h)

"""
def findTilt(self, root: Optional[TreeNode]) -> int:
    self.tilt = 0 

    def findSum(root):
        if root is None:
            return 0
        l = findSum(root.left)
        r = findSum(root.right)
        self.tilt += abs(l-r)
        return l + r + root.val
    
    findSum(root)
    return root.tilt
