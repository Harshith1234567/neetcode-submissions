# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head

        def rev(start):

            node=start

            count=0
            prev=None
            while node and count<k:
                ne=node.next
                node.next=prev
                prev=node
                node=ne
                count+=1



            return prev, start


        res=ListNode(0,head)
        dprev=res
        dnext=head
        
        while head :



            
            cu=0
            while dnext and cu<k-1:
                dnext=dnext.next
                cu+=1


            if not dnext:
                break
            nxt=dnext.next
            s,e=rev(head)


            dprev.next=s
            e.next=nxt
            

            dprev=e
            dnext=nxt
            head=nxt




        return res.next


        