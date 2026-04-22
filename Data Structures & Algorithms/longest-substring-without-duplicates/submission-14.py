class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## sliding window
        ## maintain a window without duplicate chars, use hashmap to jump ahead
        seen = {}
        l = 0
        out = 0

        for r in range(len(s)):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)
            
            seen[s[r]] = r

            print(r, l)
            out = max(r - l + 1, out)

        return out