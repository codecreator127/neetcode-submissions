class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        out = 0

        ## use backtracking
        ## choose to use current, or to use next coin

        ## this is exponential, so lets add memo to avoid computing the same things again

        memo = {}

        def backtrack(i, currAmount):
            if i >= len(coins):
                return 0
            
            if currAmount > amount:
                return 0
            
            if (i, currAmount) in memo:
                return memo[(i, currAmount)]

            if currAmount == amount:
                memo[(i, currAmount)] = 1
            else:
                memo[(i, currAmount)] = backtrack(i + 1, currAmount) + backtrack(i, currAmount + coins[i])

            return memo[(i, currAmount)]

        return backtrack(0, 0)
