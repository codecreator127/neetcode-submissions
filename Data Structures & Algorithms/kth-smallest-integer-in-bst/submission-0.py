# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # naive solution, do bfs -> list, then sort and return kth value

        from collections import deque

        queue = deque()
        queue.append(root)

        vals = []

        while queue:
            curr = queue.popleft()

            print(curr)

            if curr:
                vals.append(curr.val)
            
                queue.append(curr.left)
                queue.append(curr.right)

        
        vals.sort()

        return vals[k - 1]