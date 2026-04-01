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

        out = 0

        def dfs(root, largest):
            nonlocal out
            if not root:
                return 0

            if root.val >= largest:
                out += 1
                largest = root.val

            left = dfs(root.left, largest)
            right = dfs(root.right, largest)

        dfs(root, largest)

        return out