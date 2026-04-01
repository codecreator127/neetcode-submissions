class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        largest_container = 0

        while l < r:
            curr_container = (r - l) * min(heights[l], heights[r])

            largest_container = max(largest_container, curr_container)

            if (heights[l] > heights[r]):
                r -= 1
            else:
                l += 1

    
        return largest_container