class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        out = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0

            currSum += n

            out = max(currSum, out)

        return out