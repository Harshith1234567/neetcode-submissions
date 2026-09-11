# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        a=l1
        b=l2
        carry = 0 
        prev=l1
        aind=a
        bind=b
        if a is None:
            aind=None
        if b is None:
            bind=None

        while aind or bind:
            

        


            aval = a.val if a else 0
            bval = b.val if b else 0
            # if not a:
            #     prev.next = ListNode(0)
            if aval+bval+carry > 9:
                a.val= aval+bval+carry -10
                carry=1
            else:
                print(aval)
                a.val= aval+bval+carry 
                carry=0
            
            prev=a
            a=a.next if a else None
            b=b.next if b else None


            if a is None:
                aind=None
                
            if b is None:
                bind=None
            if a is  None and b is not None:
                prev.next = ListNode(0)
                a=prev.next

        if carry==1:
            temp = ListNode(1)
            prev.next= temp
            
        return l1

        