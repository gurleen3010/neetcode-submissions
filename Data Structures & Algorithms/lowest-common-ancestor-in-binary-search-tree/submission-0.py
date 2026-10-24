# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None

        ans = root

        while ans != None:
            if ans.val < p.val and ans.val < q.val:
                ans = ans.right
            elif ans.val > p.val and ans.val > q.val:
                ans = ans.left
            else:
                return ans

        return ans