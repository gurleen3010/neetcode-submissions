# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root is None:
            return result

        queue = []

        queue.append(root)
        level = 1

        while len(queue) > 0:
            levelLength = len(queue)

            while levelLength > 0:
                node = queue.pop(0)
                if len(result) < level:
                    result.append(node.val)

                if node.right is not None:
                    queue.append(node.right)

                if node.left is not None:
                    queue.append(node.left)

                levelLength -= 1

            level += 1

        return result