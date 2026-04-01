class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()

        out = strs[0]

        for i in range(1, len(strs)):
            while out not in strs[i]:
                out = out[:-1]

        return out