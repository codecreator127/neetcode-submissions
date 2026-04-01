class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        visited = [False] * n
        minDist = [float('inf')] * n
        minDist[0] = 0

        total = 0

        for _ in range(n):
            # pick unvisited node with smallest distance
            curr = -1
            for i in range(n):
                if not visited[i] and (curr == -1 or minDist[i] < minDist[curr]):
                    curr = i
            
            visited[curr] = True
            total += minDist[curr]

            # update distances
            x1, y1 = points[curr]

            for i in range(n):
                if not visited[i]:
                    x2, y2 = points[i]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    minDist[i] = min(minDist[i], dist)
        
        return total