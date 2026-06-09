"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ### maintain a minheap of intervals by end time
        ### sort by start time, iterate through the intervals
        ## if we find an overlap, then we open a new room
        ## maintain the num of rooms using a minheap, just check top of heap (earliest time) for overlap

        import heapq

        ## sort by start time
        intervals.sort(key=lambda x: x.start)

        heap = []

        for i in range(len(intervals)):
            curr = intervals[i]

            if heap and heap[0] <= curr.start:
                heapq.heappop(heap)
            heapq.heappush(heap, curr.end)

        return len(heap)