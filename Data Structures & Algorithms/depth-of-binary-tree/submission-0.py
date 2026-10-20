# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDepthPtr = 0

    def maxDepth_(self, root: Optional[TreeNode], height: int) -> None:
        if root == None:
            return

        height = height + 1

        self.maxDepth_(root.left, height)
        self.maxDepth_(root.right, height)

        if self.maxDepthPtr < height:
            self.maxDepthPtr = height

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth_(root, 0)

        return self.maxDepthPtr