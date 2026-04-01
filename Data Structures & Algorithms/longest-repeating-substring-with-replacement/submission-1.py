class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## key obs is window size - maxf must be <= k

        ## (right - left + 1) - maxf <= k

        left = 0
        count = {}

        maxFrequency = 0
        out = 0

        for right in range(len(s)):

            count[s[right]] = 1 + count.get(s[right], 0)

            maxFrequency = max(maxFrequency, count[s[right]])

            while (right - left + 1) - maxFrequency > k:
                count[s[left]] -= 1
                left += 1

            out = max(out, right - left + 1)

        return out

