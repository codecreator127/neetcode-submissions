class Solution:
    # def countSubstrings(self, s: str) -> int:
        # ## DP
        # out = 0
        # n = len(s)

        # dp = [[False] * n for _ in range(n)]

        # for i in range(n - 1, -1, -1):
        #     for j in range(i, n):

        #         if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True
        #             out += 1

        # return out

    def countSubstrings(self, s):
        res = 0

        for i in range(len(s)):
            res += self.countPalindrome(s, i, i)
            res += self.countPalindrome(s, i, i + 1)
        
        return res

    def countPalindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        
        return res