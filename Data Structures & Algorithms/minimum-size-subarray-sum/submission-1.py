class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ## use sliding window, since we have monotonic condition
        ## while sum current_window >= target then shrink window and take min(ans)

        l = 0
        ans = float("inf")
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1


        if ans == float("inf"):
            return 0
        return ans