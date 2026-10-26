# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)

        if root == None:
            return node

        curr, par = root, root
        while curr != None:
            par = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if val < par.val:
            par.left = node
        else:
            par.right = node

        return root