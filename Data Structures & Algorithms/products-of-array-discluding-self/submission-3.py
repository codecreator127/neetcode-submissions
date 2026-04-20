class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## brute force first

        out = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    out[i] *= nums[j]
        
        return out