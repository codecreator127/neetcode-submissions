class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def validEatingSpeed(speed: int) -> bool:

            import math

            total_time = 0

            for pile in piles:
                total_time += math.ceil(pile / speed)

            return total_time <= h

        left = 1
        right = max(piles)

        minEatingSpeed = max(piles)

        while left <= right:
            middle = (right + left) // 2

            if validEatingSpeed(middle):
                minEatingSpeed = min(middle, minEatingSpeed)

                right = middle - 1

            else:
                left = middle + 1

        
        return minEatingSpeed
            