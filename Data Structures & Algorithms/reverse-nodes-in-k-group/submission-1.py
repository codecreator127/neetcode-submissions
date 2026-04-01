# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## brute force use array to store seen nodes in order

        # seen = []
        # curr = head
        # while curr:
        #     seen.append(curr)

        #     curr = curr.next

        # if not head:
        #     return None

        # for i in range(0, len(seen), k):
        #     if i + k <= len(seen):
        #         seen[i:i + k] = reversed(seen[i:i + k])

        # for i in range(len(seen) - 1):
        #     seen[i].next = seen[i + 1]

        # seen[-1].next = None
        # return seen[0]
        

        # use a two pointer sliding window method

        # def reverseList(head, tail):
        #     if not head or not tail:
        #         return head, tail
        #     prev = tail.next
        #     curr = head

        #     while curr != tail.next:
        #         temp = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = temp

        #     return prev, head

        # leftc = 0
        # rightc = 0

        # node = head
        # left = right = node

        # dummy = ListNode()
        # dummy.next = head

        # tail1 = dummy

        # while right:
        #     rightc += 1

        #     if rightc - leftc == k:
        #         # right is guaranteed non-None here
        #         next_head = right.next

        #         head2, tail2 = reverseList(left, right)

        #         tail1.next = head2
        #         tail2.next = next_head
        #         tail1 = tail2

        #         leftc = rightc
        #         left = right = next_head
        #     else:
        #         right = right.next


        # return dummy.next

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr





                


