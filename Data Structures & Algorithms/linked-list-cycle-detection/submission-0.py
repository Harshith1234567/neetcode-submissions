# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast=head.next

        while fast and head and fast.next:
            if fast==head:
                return True
            

            fast=fast.next.next
            head=head.next

        return False
