# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list2 if not list1 else list1

        node, head = ListNode(float('-inf'), None), None

        while list1 is not None and list2 is not None:
            forw1 = list1.next
            forw2 = list2.next

            if list1.val <= list2.val:
                node.next = list1
                list1 = forw1
            else:
                node.next = list2
                list2 = forw2

            node = node.next
            node.next = None

            if head is None:
                head = node

        if list1 is not None:
            node.next = list1

        if list2 is not None:
            node.next = list2

        return head
