class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # space optimal
        
        # start by constructing the prefix array from the input
        out = [1] * len(nums)
        left = 1

        for i in range(len(nums)):
            out[i] = left
            left *= nums[i]

        # now build using the suffix array using our prefix array built in out
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * right
            right *= nums[i]

        return out