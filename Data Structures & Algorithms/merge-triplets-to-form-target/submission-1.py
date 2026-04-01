class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        validTriplets = []

        for trip in triplets:
            if trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                validTriplets.append(trip)

        print(validTriplets)

        if len(validTriplets) == 0:
            return False

        curr = validTriplets[0]
        for i in range(len(validTriplets)):            
            trip = validTriplets[i]
            
            curr = [max(curr[0], trip[0]), max(curr[1], trip[1]), max(curr[2], trip[2])]
            if curr == target:
                return True

        return False