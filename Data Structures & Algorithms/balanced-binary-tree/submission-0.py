# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced_(self, root:Optional[TreeNode]) -> tuple[bool, int]:
        if root is None:
            # isCurrentNodeBalanced, Height
            return True, 0

        leftSubtree = self.isBalanced_(root.left)
        rightSubtree = self.isBalanced_(root.right)

        return (leftSubtree[0] and rightSubtree[0] and abs(leftSubtree[1] - rightSubtree[1]) <= 1), max(leftSubtree[1], rightSubtree[1]) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalanced_(root)[0]