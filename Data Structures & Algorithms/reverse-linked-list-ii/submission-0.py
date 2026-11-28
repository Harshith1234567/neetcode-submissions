# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right==left:
            return head

        cur = head
        l=None
        r=None
        count=0
        prev=None
        p1=None
        nxt=None

        while cur and count<=right : 
            count+=1
            temp=cur
            nxt=cur.next
            if count==left:

                l=cur
                p1=prev
                # print('1',cur.val)

            elif l:
                # print('2',cur.val)
                cur.next=prev
                prev=temp
                cur=nxt
                if count==right:
                    r=temp
                    break
                
                continue



            

            cur=cur.next

            prev =temp
        
        
        if p1 is None:
            l.next=nxt

            return r

            
        p1.next=r
        l.next=nxt
        return head


        