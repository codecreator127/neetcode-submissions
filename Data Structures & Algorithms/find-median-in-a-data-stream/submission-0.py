class MedianFinder:
    import heapq

    def __init__(self):
        ## use minHeap to store nums
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)

    def findMedian(self) -> float:

        if len(self.heap) == 1:
            return self.heap[0]
        
        print(self.heap)

        print(heapq.nsmallest((len(self.heap) // 2) + 1, self.heap)[-1])

        if len(self.heap) % 2 == 0:
            median1 = heapq.nsmallest(len(self.heap) // 2, self.heap)[-1]
            median2 = heapq.nsmallest((len(self.heap) // 2) + 1, self.heap)[-1]

            return (median1 + median2) / 2
        
        return heapq.nsmallest((len(self.heap) // 2) + 1, self.heap)[-1]