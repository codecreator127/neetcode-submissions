class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 3:
            return len(set(s))

        curr = set()

        left = 0
        right = 1
        out = 1

        curr.add(s[0])

        while right < (len(s)):

            print((left, right))

            if s[right] in curr:
                while s[left] != s[right] and left < right:
                    curr.remove(s[left])
                    left += 1
                
                left += 1
            else:
                curr.add(s[right])

            out = max(out, (right - left) + 1)
            
            right += 1

        return out