class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # out = []
        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         out.append(subset.copy())
        #         return
        #     # 2 decisions
        #     # 1. include nums[i] (left branch)

        #     subset.append(nums[i])
        #     dfs(i + 1)

        #     # 2. don't include nums[i] (right branch)

        #     subset.pop()
        #     dfs(i + 1)
        
        # dfs(0)

        # return out

        out = [[]]

        for num in nums:
            out += [subset + [num] for subset in out]

        return out
