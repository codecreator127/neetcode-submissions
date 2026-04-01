class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        townJudge = trust[0][1]

        seen = set()
        seen.add(trust[0][1])

        for i in range(1, len(trust)):
            if trust[i][1] not in seen:
                return -1
        
        return townJudge