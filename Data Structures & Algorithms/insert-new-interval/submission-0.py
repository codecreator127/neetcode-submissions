class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        out = []

        for i in range(len(intervals)):
            interval = intervals[i]

            if newInterval[1] < interval[0]:
                out.append(newInterval)
                return out + intervals[i:]
            elif newInterval[0] > interval[1]:
                out.append(interval)
            else:
                newInterval = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]

        out.append(newInterval)

        return out