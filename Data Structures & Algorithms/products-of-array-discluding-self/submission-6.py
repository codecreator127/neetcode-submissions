class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and suffix approach, but space optimized
        n = len(nums)
        out = [1] * n

        ## 2 loops, 1 for suffix, 1 for prefix
        # start +1 for prefix (there is no prefix for index 0)
        
        left = 1
        for i in range(n):
            out[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(n - 1, -1, -1):
            out[i] *= right
            right *= nums[i]

        return out