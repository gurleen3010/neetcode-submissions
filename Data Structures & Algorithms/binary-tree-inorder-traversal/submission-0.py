# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        leftSubtree = self.inorderTraversal(root.left)
        rightSubtree = self.inorderTraversal(root.right)

        return leftSubtree + [root.val] + rightSubtree