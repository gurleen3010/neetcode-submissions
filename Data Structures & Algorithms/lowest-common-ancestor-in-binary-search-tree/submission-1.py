# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def lca(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
            if root is None:
                return None

            if root is not None and (root.val == p.val or root.val == q.val):
                return root

            leftlca = lca(root.left, p, q)
            rightlca = lca(root.right, p, q)

            if leftlca is not None and rightlca is not None:
                return root

            return leftlca if leftlca is not None else rightlca

        return lca(root, p, q)