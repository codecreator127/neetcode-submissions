# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        ## bfs

        if not root:
            return []

        out = []
        queue = deque()
        level = 0
        queue.append((root, level))

        while queue:

            currLevel = []
            while queue and queue[0][1] == level:
                curr = queue.popleft()[0]

                # print(curr.val)
                if not curr:
                    break
                currLevel.append(curr.val)

                if curr.left != None:
                    queue.append((curr.left, level + 1))
                
                if curr.right != None:
                    queue.append((curr.right, level + 1))

            out.append(currLevel)
            level += 1

        
        return out