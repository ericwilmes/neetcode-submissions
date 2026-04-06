# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(max_val, curr):
            if not curr:
                return 0

            new_max = max(max_val, curr.val)

            left = helper(new_max, curr.left)
            right = helper(new_max, curr.right)

            if curr.val >= max_val:
                return left + right + 1
            return left + right
        
        return helper(root.val, root)