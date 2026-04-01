class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def getProduct(nums):
            product = 1
            for n in nums:
                product *= n
            return product

        ## brute force + memo

        memo = {}

        out = min(nums)
        n = len(nums)

        for i in range(n):
            out = max(nums[i], out)
            
            for j in range(i):
                if (j, i) in memo:
                    out = max(memo[(j, i)], out)
                else:
                    product = getProduct(nums[j:i + 1])
                    out = max(product, out)

                    memo[(j, i)] = product

        return out