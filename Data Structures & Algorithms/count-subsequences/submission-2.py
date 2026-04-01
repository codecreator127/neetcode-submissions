class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        ## run backtracking on substrings of s
        ## either choose current, or skip current
        ## if substring is same length as t then do a check

        ## now optimize using memo

        memo = {}

        def backtrack(i, substring):
            if substring == t:
                return 1
            
            if i >= len(s):
                return 0
            
            if len(substring) >= len(t):
                return 0
            
            if (i, substring) in memo:
                return memo[(i, substring)]

            memo[(i, substring)] = backtrack(i + 1, substring + s[i]) + backtrack(i + 1, substring)

            return memo[(i, substring)]
        
        return backtrack(0, "")