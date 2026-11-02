# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def lengthOfLL(self, head:Optional[TreeNode]) -> int:
        if not head:
            return 0

        length = 0
        while head:
            head = head.next
            length += 1

        return length

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyHead = dummyNode
        dummyNode.next = head

        lengthLL = self.lengthOfLL(head)
        finalLen = lengthLL - n

        while finalLen > 0:
            dummyNode = dummyNode.next
            finalLen -= 1

        delNode = dummyNode.next
        dummyNode.next = dummyNode.next.next
        delNode.next = None

        return dummyHead.next