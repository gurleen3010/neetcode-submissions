# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result

        queue = []
        queue.append(root)

        while len(queue) > 0:
            currentLen = len(queue)
            miniResult = []

            while currentLen > 0:
                node = queue.pop(0)

                miniResult.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

                currentLen -= 1

            res = miniResult.copy()
            result.append(res)

        return result
        