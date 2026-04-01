class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)

        memo = {}

        def dfs(alice, i, m):
            if i == n:
                return 0
            
            if (alice, i, m) in memo:
                return memo[(alice, i, m)]

            res = 0 if alice else float("inf")

            ## up to m - 1 cases

            total = 0

            for X in range(1, 2 * m + 1):
                if i + X > len(piles):
                    break
                
                total += piles[i + X - 1]

                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(m, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(m, X)))


            memo[(alice, i, m)] = res
            return res
        
        return dfs(True, 0, 1)