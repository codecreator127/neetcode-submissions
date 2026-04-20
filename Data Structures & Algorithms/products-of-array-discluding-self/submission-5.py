class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix approach

        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        ## 2 loops, 1 for suffix, 1 for prefix
        # start +1 for prefix (there is no prefix for index 0)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        out = []

        for i in range(len(nums)):
            out.append(suffix[i] * prefix[i])

        return out