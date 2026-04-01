class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)
        out = 0

        q = deque([beginWord])

        while q:
            out += 1

            ## do 1 level of bfs
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return out
                
                for i in range(len(node)):
                    for c in range(97, 123):
                        if chr(c) == node[i]:
                            continue
                        
                        nei = node[:i] + chr(c) + node[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        
        return 0