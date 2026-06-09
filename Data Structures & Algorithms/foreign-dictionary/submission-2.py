class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        ## construct indegree array
        ## construct a node graph to traverse
        ## apply kahns algorithm

        indegree = defaultdict(int)
        graph = defaultdict(list)

        for word in words:
            for c in word:
                indegree[c] = 0

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    indegree[w2[j]] += 1
                    graph[w1[j]].append(w2[j])
                    break

        queue = deque()

        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
        
        ans = ""
        while queue:
            node = queue.popleft()
            ans += node

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(ans) != len(indegree):
            return ""
        
        return ans