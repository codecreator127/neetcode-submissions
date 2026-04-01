# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs, track the max seen thus far

        largest = root.val

        def dfs(root, largest):
            if not root:
                return 0

            res = 1 if root.val >= largest else 0
            largest = max(largest, root.val)

            res += dfs(root.left, largest)
            res += dfs(root.right, largest)

            return res

        return dfs(root, largest)