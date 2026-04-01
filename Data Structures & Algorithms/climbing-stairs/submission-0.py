class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [None] * n
        
        def check(i):
            if i >= n:
                return i == n

            if cache[i] != None:
                return cache[i]
            cache[i] = check(i + 1) + check(i + 2)

            return cache[i]

        return check(0)