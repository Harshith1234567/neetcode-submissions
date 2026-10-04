# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        if list1.val > list2.val:
            list1,list2=list2,list1
            
        res=list1

        

        p1=None
        p2=list2
        

        while list1 and list2:
            if list1.val<=list2.val:
                p1=list1
                list1=list1.next

            else:
                p2=list2.next


                # list2.next=list1.next
                # list1.next=list2
                # p1=list1
                # list1=list2

                p1.next=list2
                list2.next=list1
                p1=list2


                list2=p2


        if list2:
            p1.next=list2

        return res


        