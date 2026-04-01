# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## split into 2
        
        p1 = head
        p2 = head.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        # now p1 is at exactly half, so now split from p1.next onwards


        half2 = p1.next

        prev = None
        curr = half2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head2 = prev
        
        ## split off two halves
        p1.next = None
        ## now merge them alternating starting from head 1 up until p1
        curr = head
        while curr:
            temp = curr.next

            curr.next = head2
            curr = curr.next

            head2 = temp


