class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ## try backtracking

        shorter = text1
        longer = text2

        if len(text1) > len(text2):
            longer = text1
            shorter = text2

        memo = [[None] * len(longer) for _ in range(len(shorter))]

        print(memo)

        def backtrack(i, j):
            if i > len(shorter) - 1 or j > len(longer) - 1:
                return 0
            
            if memo[i][j] != None:
                return memo[i][j]
            
            if shorter[i] == longer[j]:
                memo[i][j] = 1 + backtrack(i + 1, j + 1)
                return memo[i][j]
            else:
                memo[i][j] = max(backtrack(i + 1, j), backtrack(i, j + 1))
                return memo[i][j]

        backtrack(0, 0)

        print(memo)

        return memo[0][0]