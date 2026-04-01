class Solution:
    def longestPalindrome(self, s: str) -> str:

        ## brute force

        out = ""

        for i in range(len(s)):
            for j in range(i, len(s)):

                curr = s[i:j + 1]

                print(curr)

                if curr == curr[::-1] and len(curr) > len(out):
                    out = curr

        
        return out