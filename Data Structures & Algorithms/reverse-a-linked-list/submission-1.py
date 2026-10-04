# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        p=None
        if head:
            n=head.next

        while head:
            head.next=p
            p=head
            head=n
            if n:
                n=n.next

        return p

            