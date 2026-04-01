class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ## bracktrack

        ## 2 choices, partition at that point, or don't partition

        out = []

        subset = []

        def backtrack(i, j):
            if j >= len(s):
                out.append(subset.copy())
                return

            if i >= len(s):
                return

            ## choose to partition if palindrome
            substring = s[j : i + 1]
            if substring == substring[::-1]:
                subset.append(substring)

                backtrack(i + 1, j = i + 1)

                subset.pop()
                ## choose not to partition if not palindrome
                backtrack(i + 1, j)
            else:
                backtrack(i + 1, j)

        backtrack(0, 0)
        return out