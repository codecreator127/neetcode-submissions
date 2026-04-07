class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        out = ""

        while p1 < len(word1) and p1 < len(word2):
            out += word1[p1]
            out += word2[p1]

            p1 += 1
        
        while p1 < len(word1):
            out += word1[p1]
            p1 += 1
        
        while p1 < len(word2):
            out += word2[p1]
            p1 += 1
        
        return out