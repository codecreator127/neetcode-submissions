class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ## brute force
        ## go through the array for each task
        ## sort the tasks by enqueue time
        ## better, convert to hashmap, key = value, and value is the index

        ## use a minheap to track

        import heapq

        n = len(tasks)
        tasks = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        tasks.sort()

        
        result = []
        pq = []
        time = 0
        i = 0

        while i < n or pq:
            if not pq:
                time = max(time, tasks[i][0])

            while i < n and tasks[i][0] <= time:
                e, p, idx = tasks[i]
                heapq.heappush(pq, (p, idx))
                i += 1

            p, idx = heapq.heappop(pq)
            time += p
            result.append(idx)

        return result

        
