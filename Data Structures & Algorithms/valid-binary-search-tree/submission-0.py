
class Solution:
    class isBSTClass:
        def __init__(self, minVal, maxVal, isBST):
            self.minVal = minVal
            self.maxVal = maxVal
            self.isBST = isBST

    def isValidBST_(self, root: Optional[TreeNode]) -> isBSTClass:
        if root is None:
            return self.isBSTClass(
                float('inf'), float('-inf'), True
            )

        leftSubtree = self.isValidBST_(root.left)
        rightSubtree = self.isValidBST_(root.right)

        isCurrentNodeBST = (
            leftSubtree.isBST
            and rightSubtree.isBST
            and root.val > leftSubtree.maxVal
            and root.val < rightSubtree.minVal
        )

        currentNodeMinVal = min(leftSubtree.minVal, root.val)
        currentNodeMaxVal = max(rightSubtree.maxVal, root.val)

        return self.isBSTClass(
            currentNodeMinVal,
            currentNodeMaxVal,
            isCurrentNodeBST
        )

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBST_(root).isBST
