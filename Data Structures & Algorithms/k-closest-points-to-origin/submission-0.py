class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq, math

        minHeap = []

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            heapq.heappush(minHeap, (-math.sqrt(x*x + y*y), i))

            while len(minHeap) > k:
                heapq.heappop(minHeap)

        
        out = []

        for p in minHeap:
            out.append(points[p[1]])

        return out


        
