class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if word1 == word2:
            return 0
        

        ## 3 decisions, do dfs and find the minimum cost

        memo = {}

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return min(1 + dfs(i + 1, j), 1 + dfs(i + 1, j + 1), 1 + dfs(i, j + 1))
            
        return dfs(0, 0)