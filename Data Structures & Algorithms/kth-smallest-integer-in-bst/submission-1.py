# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # morris

        count = 0
        item = None

        def dfs(node):
            nonlocal count
            nonlocal item
            if not node:
                return
            print(count)
            
            dfs(node.left)
            count += 1
            if count == k and not item:
                item = node.val
                return
            dfs(node.right)

        dfs(root)
        return item