# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev = None
        curr = head

        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        ## 1. Find mid
        midNode = self.findMid(head)

        head1, brokenHead = head, midNode.next
        newHead = head1

        midNode.next = None

        head2 = self.reverse(brokenHead)

        while head2:
            c3 = head1.next
            c4 = head2.next

            head1.next = head2
            head2.next = c3

            head1 = c3
            head2 = c4