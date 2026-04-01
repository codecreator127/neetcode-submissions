class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        ## do bfs

        ## at each round of bfs, increment counter by 1
        ## and go through all possible changes but just check for if word in wordList

        words = set(wordList)
        q = deque([beginWord])

        count = 0

        letters = "abcdefghijklmnopqrstuvwxyz"

        while q:
            count += 1

            ## do 1 level of bfs at a time
            for _ in range(len(q)):
                currWord = q.popleft()

                # base end condition
                if currWord == endWord:
                    return count
                
                ## otherwise check all possibilities
                for i in range(len(currWord)):
                    for letter in letters:
                        if currWord[i] == letter:
                            continue

                        neighborWord = currWord[:i] + letter + currWord[i + 1:]
                        if neighborWord in words:
                            q.append(neighborWord)
                            words.remove(neighborWord)
        

        return 0



