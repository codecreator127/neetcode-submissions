class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        maxHeap = []

        for rock in stones:
            heapq.heappush(maxHeap, -rock)

        while len(maxHeap) > 1:
            rock1 = heapq.heappop(maxHeap)
            rock2 = heapq.heappop(maxHeap)

            print(rock1)
            print(rock2)

            if rock1 == rock2:
                continue
            else:
                rock2 = -rock1 - -rock2
                heapq.heappush(maxHeap, -rock2)

        if maxHeap:
            return -maxHeap[0]

        return 0