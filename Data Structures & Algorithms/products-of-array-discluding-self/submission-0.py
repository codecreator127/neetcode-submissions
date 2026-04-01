class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intuition: brute force

        out = []
        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)):
                
                if j != i:
                    curr *= nums[j]

            
            out.append(curr)

        return out