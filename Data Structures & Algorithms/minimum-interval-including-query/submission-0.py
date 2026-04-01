class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        ## brute force

        intervals = sorted(intervals, key=lambda x:x[0])

        out = []
        for num in queries:
            curr = 99999
            for interval in intervals:
                if interval[0] <= num <= interval[1]:
                    curr = min(curr, interval[1] - interval[0] + 1)
            
            if curr == 99999:
                out.append(-1)
            else:
                out.append(curr)

        return out