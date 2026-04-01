# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## brute force use array to store seen nodes in order

        seen = []
        curr = head
        while curr:
            seen.append(curr)

            curr = curr.next

        
        if not head:
            return None

        for i in range(0, len(seen), k):
            if i + k <= len(seen):
                seen[i:i + k] = reversed(seen[i:i + k])

        for i in range(len(seen) - 1):
            seen[i].next = seen[i + 1]

        seen[-1].next = None
        return seen[0]
        

        # use a two pointer sliding window method

