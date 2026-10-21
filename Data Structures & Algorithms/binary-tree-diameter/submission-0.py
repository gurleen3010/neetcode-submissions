# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    class Diameter:
        def __init__(self, currentHt = 0, maxDia = 0):
            self.currentHt = currentHt
            self.maxDia = maxDia

    def diameter_(self, root: Optional[TreeNode]) -> "Solution.Diameter":
        if root is None:
            return self.Diameter(0,0)

        leftSubtree = self.diameter_(root.left)
        rightSubtree = self.diameter_(root.right)

        currentNodeHeight = max(leftSubtree.currentHt, rightSubtree.currentHt) + 1
        currentNodeDiameter = leftSubtree.currentHt + rightSubtree.currentHt
        currentNodeMaxDiameter = max(max(leftSubtree.maxDia, rightSubtree.maxDia), currentNodeDiameter)

        return self.Diameter(currentNodeHeight, currentNodeMaxDiameter)
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.diameter_(root).maxDia