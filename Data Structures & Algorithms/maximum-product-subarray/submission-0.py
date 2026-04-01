class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def getProduct(nums):

            product = 1

            print(nums)

            for n in nums:
                product *= n

                print(product)

            return product

        ## brute force

        out = min(nums)

        n = len(nums)

        for i in range(n):
            out = max(nums[i], out)
            
            for j in range(i):
                out = max(getProduct(nums[j:i + 1]), out)

        return out