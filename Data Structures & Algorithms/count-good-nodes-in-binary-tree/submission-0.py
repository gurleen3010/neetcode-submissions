# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # At every node check the count of the good tree nodes
    def goodNodes_(self, root: TreeNode, maximum: int) -> int:
        if root is None:
            return 0

        count = 0
        if root.val >= maximum:
            count += 1

        maximumSoFar = max(maximum, root.val)
        leftSubtree = self.goodNodes_(root.left, maximumSoFar)
        rightSubtree = self.goodNodes_(root.right, maximumSoFar)

        return leftSubtree + rightSubtree + count

    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodes_(root, float('-inf'))