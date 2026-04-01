class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        
        if total_length % 4 != 0:
            return False

        length = total_length // 4

        sides = [0] * 4

        matchsticks.sort(reverse=True)

        def dfs(i):
            if i == len(matchsticks):
                return True

            ## choose 1 of 4 paths

            match = matchsticks[i]
            
            for j in range(len(sides)):
                if sides[j] + match <= length:

                    sides[j] += match
                    if dfs(i + 1):
                        return True
                    
                    sides[j] -= match

                if sides[j] == 0:
                    break

            return False
        
        return dfs(0)