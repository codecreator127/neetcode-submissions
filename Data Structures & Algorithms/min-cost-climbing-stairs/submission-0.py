class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [None] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0

            if cache[i] != None:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return cache[i]

        return min(dfs(0), dfs(1))