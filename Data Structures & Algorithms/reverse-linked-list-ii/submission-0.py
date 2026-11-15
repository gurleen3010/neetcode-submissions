# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev, curr = None, head

        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw

        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return None

        dummyNode = ListNode(0)
        dummyHead = dummyNode

        dummyHead.next = head
        leftPtr, rightPtr = dummyHead, dummyHead

        while left - 1 > 0:
            leftPtr = leftPtr.next
            left -= 1

        while right > 0:
            rightPtr = rightPtr.next
            right -= 1

        listToBeReversedHead = leftPtr.next
        listToBeReversedTail = rightPtr

        brokenRHS = listToBeReversedTail.next

        leftPtr.next = None
        listToBeReversedTail.next = None

        reversedListHead = self.reverse(listToBeReversedHead)

        leftPtr.next = reversedListHead
        listToBeReversedHead.next = brokenRHS

        return dummyHead.next

