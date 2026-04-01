class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProd = minProd = out = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            prevMax = maxProd

            maxProd = max(x, x * maxProd, x * minProd)
            minProd = min(x, x * minProd, x * prevMax)

            out = max(out, maxProd)

        return out