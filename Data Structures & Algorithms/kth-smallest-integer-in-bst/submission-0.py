# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        value = -1

        def kthSmallest_(root: Optional[TreeNode]) -> None:
            nonlocal k, value
            
            if not root:
                return

            kthSmallest_(root.left)

            k -= 1
            if k == 0:
                value = root.val

            kthSmallest_(root.right)

        kthSmallest_(root)
        return value
            
        