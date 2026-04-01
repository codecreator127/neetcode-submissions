class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # out = []

        # for right in range(k, len(nums) + 1):
        #     print(nums[right - k : right])
        #     out.append(max(nums[right - k : right]))

        # return out


        # using a heap
        import heapq

        max_heap = []

        out = []
        left = 0

        for right in range(len(nums)):
            heapq.heappush_max(max_heap, (nums[right], right))
            print(max_heap)

            while max_heap[0][1] <= (right - k):
                heapq.heappop_max(max_heap)

                print(max_heap)

            if (right - left + 1) >= k:
                out.append(max_heap[0][0])

        return out
