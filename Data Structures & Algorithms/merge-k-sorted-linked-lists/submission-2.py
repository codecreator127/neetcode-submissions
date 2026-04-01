# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge2Lists(list1, list2):
    dummy = node = ListNode()

    while list1 and list2:

        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next

        node = node.next
    
    node.next = list1 or list2

    return dummy.next


class Solution:
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ## brute force
        # all_vals = []

        # for head in lists:
        #     while head:
        #         all_vals.append(head)
        #         head = head.next

        # if len(all_vals) == 0:
        #     return None
        
        # all_vals.sort(key=lambda node: node.val)

        # for i in range(len(all_vals) - 1):
        #     all_vals[i].next = all_vals[i + 1]

        # return all_vals[0]

        ## iteratively merge the lists with the next one

        if len(lists) == 0:
            return None

        i = 0
        while i < len(lists) - 1:
            merged_head = merge2Lists(lists[i], lists[i + 1])
            lists[i + 1] = merged_head

            i += 1
        


        return lists[-1]

