# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        vals = []

        def trav(root, depth):
            if not root:
                return None

            if depth == len(vals):
                vals.append(root.val)

            trav(root.right, depth+1)
            trav(root.left, depth+1)

        trav(root, 0)
        return vals