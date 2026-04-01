"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        ## do a double sorting
        ## sort by start time
        ## sort by end time

        ## if the at the same i there is overlap then its false

        startTimeSorted = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(intervals)):
            if startTimeSorted[i].start < startTimeSorted[i - 1].end:
                return False

        return True