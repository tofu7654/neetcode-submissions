# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0

            # we get the depths of the right and left children
            left = dfs(root.left)
            right = dfs(root.right)

            # add those to get the diameter
            self.res = max(self.res, left + right)

            # we send 1 + max depth to parent to calculate diameter for them
            return 1 + max(left, right)

        dfs(root)
        return self.res