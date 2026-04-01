"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ## dfs
        if not node:
            return None
        
        created = {}

        def dfs(curr):
            ##create clone of current
            if curr in created:
                return created[curr]

            copy = Node(curr.val)
            created[curr] = copy

            for n in curr.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        dfs(node)

        return created[node]