# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def __init__(self):
        self.yes = False 
         
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.checkEquality(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def checkEquality(self, root, subRoot):
        if not subRoot and not root:
            return True
        if root and subRoot and root.val == subRoot.val:
            left_equality = self.checkEquality(root.left, subRoot.left)
            right_equality = self.checkEquality(root.right, subRoot.right)

            return left_equality and right_equality
        return False
