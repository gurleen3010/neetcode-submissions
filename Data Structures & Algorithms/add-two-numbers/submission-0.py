# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        curr = dummyNode

        ptr1, ptr2 = l1, l2
        carry = 0

        while ptr1 or ptr2 or carry != 0:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0

            value = val1 + val2 + carry
            ans = value % 10
            carry = value // 10

            node = ListNode(ans)
            curr.next = node
            curr = curr.next

            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next

        return dummyNode.next

        

