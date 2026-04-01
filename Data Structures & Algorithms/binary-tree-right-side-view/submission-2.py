# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs but only take the most right node at level

        from collections import deque

        queue = deque()
        queue.append(root)

        out = []

        while queue:

            right = queue[-1]
            if right:
                out.append(right.val)

            print(right)

            qLen = len(queue)

            for i in range(qLen):
                curr = queue.popleft()
                if curr:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)

        return out
            

