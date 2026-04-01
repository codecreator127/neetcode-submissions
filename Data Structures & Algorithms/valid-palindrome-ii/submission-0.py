class Solution:
    def validPalindrome(self, s: str) -> bool:
        ## brute force

        for i in range(len(s)):
            word = s[0:i] + s[i + 1:]

            if word == word[::-1]:
                return True
        
        return False