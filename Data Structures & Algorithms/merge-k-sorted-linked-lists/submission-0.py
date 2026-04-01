# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ## brute force
        all_vals = []

        for head in lists:
            while head:
                all_vals.append(head)
                head = head.next

        if len(all_vals) == 0:
            return None
        
        all_vals.sort(key=lambda node: node.val)

        for i in range(len(all_vals) - 1):
            all_vals[i].next = all_vals[i + 1]

        return all_vals[0]