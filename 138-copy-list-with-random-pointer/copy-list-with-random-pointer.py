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
        copyMap = {None:None}

        curr = head 

        while curr:
            copyNode = Node(curr.val)
            copyMap[curr] = copyNode
            curr = curr.next
        
        curr2 = head

        while curr2:
            NewNode = copyMap[curr2]
            NewNode.next = copyMap[curr2.next]
            NewNode.random = copyMap[curr2.random]
            curr2 = curr2.next
        
        return copyMap[head]