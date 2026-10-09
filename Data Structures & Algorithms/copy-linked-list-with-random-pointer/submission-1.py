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
        dic={None:None}
        curr=head

        while curr:
            dic[curr]=Node(curr.val)
            curr=curr.next

        curr=head

        while curr:
            t=dic[curr]

            t.next=dic[curr.next]
            t.random=dic[curr.random]
            curr=curr.next

        return dic[head]