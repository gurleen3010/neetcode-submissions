"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashtable = {}

        def copyRL(head: 'Optional[Node]') -> 'Optional[Node]':
            if head is None:
                return None

            # create a clone
            hashtable[head] = Node(head.val)

            # move to next node
            hashtable[head].next = copyRL(head.next)

            # while coming back set next and random nodes because entire list has been traversed
            if head.random:
                hashtable[head].random = hashtable[head.random]

            # return newly created head
            return hashtable[head]

        return copyRL(head)