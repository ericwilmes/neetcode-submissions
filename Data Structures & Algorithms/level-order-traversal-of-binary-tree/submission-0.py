# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.levels = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root, 0)
        return self.levels

    def traverse(self, root, depth):
        if not root:
            return None
        if len(self.levels) - 1 < depth:
            self.levels.append([])

        self.levels[depth].append(root.val)
        self.traverse(root.left, depth+1)
        self.traverse(root.right, depth+1)
