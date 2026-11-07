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
        curr = head

        while curr != None:
            hashtable[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        headNew = None

        while curr != None:

            newListCurrNode = hashtable[curr]
            newListCurrNodeNext = hashtable[curr.next] if curr.next else None
            newListCurrNodeRandom = hashtable[curr.random] if curr.random else None

            newListCurrNode.next = newListCurrNodeNext
            newListCurrNode.random = newListCurrNodeRandom

            if headNew is None:
                headNew = newListCurrNode

            curr = curr.next

        return headNew