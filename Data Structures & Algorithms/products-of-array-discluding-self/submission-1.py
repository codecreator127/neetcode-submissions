class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intuition: brute force O(n^2)

        # out = []
        # for i in range(len(nums)):
        #     curr = 1
        #     for j in range(len(nums)):
                
        #         if j != i:
        #             curr *= nums[j]

            
        #     out.append(curr)

        # return out


        # use array to store calculated values to avoid recalculating
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res




