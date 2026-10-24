# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False

        if p is None and q is None:
            return True

        if p.val != q.val:
            return False
            
        leftSubtreeEquivalence = self.isSameTree(p.left, q.left)
        rightSubtreeEquivalence = self.isSameTree(p.right, q.right)

        return leftSubtreeEquivalence and rightSubtreeEquivalence

    def findNode(self, root: Optional[TreeNode], value: int) -> None:
        if root is None:
            return

        if root.val == value:
            self.sameValueNodes.append(root)

        self.findNode(root.left, value)
        self.findNode(root.right, value)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            if root is None and subRoot is None:
                return True
            else:
                return False

        if(root.val == subRoot.val):
            if (self.isSameTree(root, subRoot)):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)