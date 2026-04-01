class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # import heapq
        # minHeap = []

        # for num in nums:
        #     heapq.heappush(minHeap, num)

        
        # while len(minHeap) > k:
        #     heapq.heappop(minHeap)

        # print(minHeap)
        # return minHeap[0]
        return heapq.nlargest(k, nums)[-1]