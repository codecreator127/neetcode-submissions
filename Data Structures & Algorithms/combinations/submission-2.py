class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        import copy
        ## backtracking

        out = []

        def backtrack(i, curr):

            # print(curr)
            if len(curr) == k:
                # print(curr)
                out.append(curr.copy())
                return

            if i > n:
                return

            curr.append(i)
            backtrack(i + 1, curr)

            curr.remove(i)
            backtrack(i + 1, curr)

        backtrack(1, [])

        return out
