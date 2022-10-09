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
        if not head:
            return 
        
        curr = head
        while curr:
            cop = Node(curr.val)
            cop.next = curr.next
            curr.next = cop
            curr = curr.next.next
        
        curr = head
        while curr:
            # print(curr.val, curr.next)
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        lsc = head.next
        curr = head
        while curr:
            ornex = curr.next.next
            co = curr.next
            curr.next = ornex
            if ornex:
                co.next = ornex.next
            # print(curr.val, co.val)
            curr = ornex
        return lsc
            
            