"""
110. Balanced Binary Tree
"""

class Solution(object):
    def isBalanced(self, root):
        
        balanced = [True]

        def height(root):
            if not root:
                return 0 
        
            left_height = height(root.left)
            if balanced[0] == False:
                return 0

            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0 
            
            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0]        
