# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists)>1:
            t=[]
            for i in range(0,len(lists),2):
                li=self.mergeList(lists[i], lists[i+1] if i<len(lists)-1 else None)
                t.append(li)
            lists=t


        return lists[0]

    def mergeList(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1 and l2:
            if l2.val<l1.val:
                l1,l2=l2,l1

        head=l1
        t1,t2=l1,None
        while l1 and l2:
            if l1.val<=l2.val:
                t1=l1
                l1=l1.next
                continue
            else:
                t2=l2.next
                t1.next=l2
                l2.next=l1
                t1=t1.next
                l2=t2

        if l2:
            t1.next=l2




        return head