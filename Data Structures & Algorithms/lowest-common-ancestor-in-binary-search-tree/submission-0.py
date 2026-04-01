# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root

        while curr:
            if p.val <= curr.val and curr.val <= q.val:
                return curr
            if q.val <= curr.val and curr.val <= p.val:
                return curr

            if curr.val < q.val and curr.val < p.val:
                curr = curr.right

            elif curr.val > q.val and curr.val > p.val:
                curr = curr.left

        return curr