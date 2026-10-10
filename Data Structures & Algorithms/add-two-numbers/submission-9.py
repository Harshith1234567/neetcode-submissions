# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res=0
        car=0
        head=res=ListNode(0)

        while l1 or l2 or car:
            t1,t2=0,0
            if l1:
                t1=l1.val
                l1=l1.next

            if l2:
                t2=l2.val

            
                l2=l2.next


            res.next=ListNode((t1+t2+car)%10)
            res=res.next

            car=int((t1+t2+car)/10)

        return head.next


