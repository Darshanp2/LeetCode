"""
236. Lowest Common Ancestor of a Binary Tree
Time Complexity: O(n)
Space Complexity: O(1)  if not counting recursive stack frames, otherwise O(n)

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root is p or root is q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r