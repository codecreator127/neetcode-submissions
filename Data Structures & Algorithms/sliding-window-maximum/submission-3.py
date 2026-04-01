class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # out = []

        # for right in range(k, len(nums) + 1):
        #     print(nums[right - k : right])
        #     out.append(max(nums[right - k : right]))

        # return out


        # using a heap
        # import heapq

        # max_heap = []

        # out = []
        # left = 0

        # for right in range(len(nums)):
        #     heapq.heappush_max(max_heap, (nums[right], right))

        #     while max_heap[0][1] <= (right - k):
        #         heapq.heappop_max(max_heap)

        #     if (right - left + 1) >= k:
        #         out.append(max_heap[0][0])

        # return out


        # using a deque

        out = []

        q = deque()

        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                out.append(nums[q[0]])
                l += 1
            r += 1
        return out