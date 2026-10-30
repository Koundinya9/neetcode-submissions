# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        cache = {}
        

        def rec(node, rob):
            if not node:
                return 0
            if (node, rob) in cache:
                return cache[(node, rob)]

            if rob:
                cache[(node, rob)] = max(node.val + rec(node.left, not rob) + rec(node.right, not rob), rec(node.left, rob) + rec(node.right, rob))

            if not rob:
                cache[(node, rob)] = rec(node.left, not rob) + rec(node.right, not rob)

            return cache[(node, rob)]

        return rec(root, True)