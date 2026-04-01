class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## use priority queue

        ## first hash into a hashmap, counting frequency, then place in priority queue

        count = Counter(tasks)
        maxHeap = [-counts for counts in count.values()]

        heapq.heapify(maxHeap)

        time = 0

        q = deque() # pairs of [-counts, ,idletime]

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                counts = 1 + heapq.heappop(maxHeap)
                if counts:
                    q.append([counts, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

        