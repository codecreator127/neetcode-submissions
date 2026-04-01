class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        ## run backtracking on substrings of s
        ## either choose current, or skip current
        ## if substring is same length as t then do a check

        def backtrack(i, substring):
            if substring == t:
                return 1
            
            if i >= len(s):
                return 0
            
            if len(substring) >= len(t):
                return 0
            
            return backtrack(i + 1, substring + s[i]) + backtrack(i + 1, substring)
        
        return backtrack(0, "")