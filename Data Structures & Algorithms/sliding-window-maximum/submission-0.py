class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        out = []

        for right in range(k, len(nums) + 1):
            print(nums[right - k : right])
            out.append(max(nums[right - k : right]))

        return out


        # import heapq

        # max_heap = []

        # out = []
        # left = 0

        # # first iterate through first window
        # for right in range(len(nums)):
        #     heapq.heappush(max_heap, (nums[right], right))

        #     if (right - left + 1) >= k:
        #         out.append(max_heap[-1][0])

        #     while max_heap[-1][1] < (right - k):
        #         max_heap.heappop()

            
        # return out
