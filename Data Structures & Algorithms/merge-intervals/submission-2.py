class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ## greedy approach
        intervals = sorted(intervals, key=lambda interval:interval[0])

        out = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]

            last = out[-1]

            if last[1] >= interval[0]:
                out[-1] = [
                    min(last[0], interval[0]),
                    max(last[1], interval[1])
                ]
            else:
                out.append(interval)

        return out